import plotly.graph_objects as go
import numpy as np

#insert array here
array = [
    [12, 18, 25, 30, 22],
    [15, 20, 28, 35, 27],
    [10, 14, 19, 23, 18],
    [40, 45, 50, 55, 48],
    [33, 37, 42, 46, 39]
]
z_data = np.array(array)
z_norm = 255 * (z_data-z_data.min()) / (z_data.max() - z_data.min())
z_norm = z_norm.astype(np.uint8)

coordinates = [
    [-76.20495, 43.09195], #top left
    [-76.08305, 43.09195], #top right
    [-76.08305, 43.00185], #bottom-right
    [-76.20495, 43.00185] #bottom-left
]

fig = go.Figure()

fig.update_layout(
    mapbox=dict(
        style="open-street-map",
        center=dict(lat=43.0469, lon=-76.144),
        zoom=12,
        layers=[
            dict(
                sourcetype="image",
                source=z_norm,
                coordinates=coordinates,
                opacity=0.6
            )
        ]
    ),
    width=700,
    height=700,
    title="Crime Density Overlay (10km by 10km)"
)
fig.show()