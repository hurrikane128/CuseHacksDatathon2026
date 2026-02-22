import plotly.graph_objects as go
import matplotlib
import numpy as np
import os
import math
import base64
from PIL import Image
from io import BytesIO

import maptoken
import Parameters as params

# Convert heatmap to base64 PNG
def encode_png(arr):
    buffer = BytesIO()
    Image.fromarray(arr).save(buffer, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode()

# -----------------------------
# TRUE 10×10 KM SQUARE USING WEB MERCATOR METERS
# -----------------------------
def lon_to_mx(lon): return lon * 20037508.34 / 180
def lat_to_my(lat): return math.log(math.tan((math.pi/4) + (math.radians(lat)/2))) * 20037508.34 / math.pi
def mx_to_lon(mx): return mx * 180 / 20037508.34
def my_to_lat(my): return math.degrees(2 * math.atan(math.exp(my * math.pi / 20037508.34)) - math.pi/2)

def getCrimeCountArray( crime_map ):
    crime_count = []
    for y in range(params.CRIME_MAP_HEIGHT):
        temp = []
        for x in range(params.CRIME_MAP_WIDTH):
            num = 0
            d = crime_map[y][x]
            for i in d.keys():
                num += d[i]
            temp.append(num)
        crime_count.append(temp)
    return crime_count

def generateHeatMap( crime_map ):
    # Load and resize map image (256×256)
    img = Image.open("Syracuse_Map.png").convert("RGB").resize((256, 256), Image.NEAREST)

    # Set Mapbox token
    os.environ["MAPBOX_ACCESS_TOKEN"] = maptoken.maptoken

    # Colormap
    plasma = matplotlib.colormaps.get_cmap("plasma")

    # 25×25 heatmap (0.4 km per cell for a 10 km square)
    z = getCrimeCountArray(crime_map)
    z_np = np.array(z)
    z_norm = (z_np - z_np.min()) / (z_np.max() - z_np.min())
    z_log = np.log1p(z)
    z_norm = (z_log - z_log.min()) / (z_log.max() - z_log.min())
    print(z)
    print(z_np)
    rgb_img = (plasma(z_norm)[:, :, :3] * 255).astype(np.uint8)

    # Upscale heatmap to 256×256
    rgb_img = np.array(Image.fromarray(rgb_img).resize((256, 256), Image.NEAREST))

    # Convert heatmap to base64 PNG
    encoded_heatmap = encode_png(rgb_img)

    # TRUE geographic centroid of Syracuse
    lat0 = 43.048122
    lon0 = -76.147424

    # Convert center to meters
    mx = lon_to_mx(lon0)
    my = lat_to_my(lat0)

    # Half-size of the box in meters (10 km → 5000 m each direction)
    half = 5000

    # Corners in meters
    corners_m = [
        (mx - half, my + half),
        (mx + half, my + half),
        (mx + half, my - half),
        (mx - half, my - half)
    ]

    # Convert corners back to lat/lon
    coordinates = [[mx_to_lon(x), my_to_lat(y)] for x, y in corners_m]

    # -----------------------------

    fig = go.Figure()

    # Dummy trace to activate Mapbox
    fig.add_trace(go.Scattermapbox(lat=[lat0], lon=[lon0], mode="markers",
                                   marker=dict(size=1, opacity=0)))
    fig.add_trace(go.Heatmap(
        z=z,
        colorscale="Plasma",
        showscale=True,
        opacity=0,
        hoverinfo="skip"
    ))
    fig.update_layout(
        mapbox=dict(
            accesstoken=os.environ["MAPBOX_ACCESS_TOKEN"],
            style="streets",
            center=dict(lat=lat0, lon=lon0),
            zoom=11.8,
            layers=[
                dict(
                    sourcetype="image",
                    source=encoded_heatmap,
                    coordinates=coordinates,
                    opacity=0.50,
                    below=""
                )
            ]
        ),
        width=700,
        height=700,
        title="Crime Density Overlay (True 10×10 km Square, Evenly Centered on Syracuse)"
    )

    fig.show(renderer="browser")