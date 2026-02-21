import plotly.graph_objects as go
import numpy as np
#insert array here
Array = [
    [12, 18, 25, 30, 22],
    [15, 20, 28, 35, 27],
    [10, 14, 19, 23, 18],
    [40, 45, 50, 55, 48],
    [33, 37, 42, 46, 39]
]
z_data = np.array(Array)

fig = go.Figure(data=go.Heatmap(
    z=z_data,
    colorscale="Plasma",
    colorbar=dict(title="Density")
))
fig.update_layout(
    title="Density of crime",
    xaxis_title="",
    yaxis_title="",
    width=600,
    height=600
)
fig.show()