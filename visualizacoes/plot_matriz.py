import plotly.graph_objects as go
import numpy as np

def plot_matriz_como_heatmap(matriz, titulo="Matriz"):
    fig = go.Figure(data=go.Heatmap(
        z=matriz,
        colorscale='Viridis',
        showscale=True
    ))
    fig.update_layout(
        title=titulo,
        xaxis_title="Coluna",
        yaxis_title="Linha"
    )
    return fig

