import plotly.graph_objects as go
import numpy as np
#insert array here
Array = [
    []
]
z_data = np.array(Array)

fig = go.figure(data=go.Heatmap(
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