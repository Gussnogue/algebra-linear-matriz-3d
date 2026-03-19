import plotly.graph_objects as go
import numpy as np

def plot_autovetores(autovalores, autovetores):
    # Cria uma figura 3D com os autovetores como setas
    fig = go.Figure()
    # Adicionar os autovetores como vetores
    for i in range(autovetores.shape[1]):
        v = autovetores[:, i]
        fig.add_trace(go.Scatter3d(
            x=[0, v[0]], y=[0, v[1]], z=[0, v[2]],
            mode='lines+markers',
            name=f'Autovetor {i+1} (λ={autovalores[i]:.2f})',
            line=dict(width=5)
        ))
    fig.update_layout(
        title="Autovetores no Espaço 3D",
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        )
    )
    return fig

