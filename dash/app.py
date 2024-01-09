import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import numpy as np

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='angry-birds-game', config={'editable': True}),
    dcc.RangeSlider(
        id='slingshot',
        marks={i: str(i) for i in range(-10, 11)},
        min=-10,
        max=10,
        step=1,
        value=[0, 0]
    ),
])


@app.callback(
    Output('angry-birds-game', 'figure'),
    Input('slingshot', 'value'),
)
def update_game(slingshot_values):
    bird_x = slingshot_values[0]
    bird_y = 0
    target_x = 8
    target_y = np.random.uniform(-5, 5)

    fig = px.scatter(x=[bird_x, target_x], y=[bird_y, target_y], text=['Bird', 'Target'],
                     labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Angry Birds Game')
    
    fig.update_layout(shapes=[
        {'type': 'line', 'x0': slingshot_values[0], 'y0': 0, 'x1': slingshot_values[1], 'y1': 0, 'line': {'color': 'red'}}
    ])

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
