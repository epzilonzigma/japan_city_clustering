import pandas as pd
from utils.data_prep import create_master_dataframe

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px

# set up app instance
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css', # plotly css
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css', # bootstrap css
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1.0"}])

# load data

data_path = '../data'

df = create_master_dataframe(data_path)

metric_headers = list(df.columns[2:])
metric_headers.remove('Prefecture')
metric_headers.remove('Municipality')

# app layout

app.layout = html.Div(
    id = 'root',
    children = [
        html.Div(
            id = 'header',
            children = [
                html.H3(children = '2015 Japanese Municipality Census Demographic Data'),
                html.P(
                    id = 'description',
                    children = 'Illustrates demographic metrics of a municipal level on a bar chart.'
                    )
            ]
        ),

        html.H5('Prefecture:'),

        dcc.Dropdown(id = 'prefecture_selection',
            options = [{'label': x, 'value': x} for x in list(df.Prefecture.unique())],
            multi = False,
            value = 'Tokyo',
            style = {'width':'60%'}
        ),

        html.H5('Metric:'),

        dcc.Dropdown(id = 'demographic_metrics',
            options = [{'label': x, 'value': x} for x in metric_headers],
            multi = False,
            value = metric_headers[0],
            style = {'width':'60%'}
        ),

        html.Div(id='metric_label', children = []),

        html.Br(),

        dcc.Graph(id='bar_chart', figure = {})
    ]
)

# callback function to render content on graphs
@app.callback(
    [Output(component_id = 'metric_label', component_property = 'children'),
    Output(component_id = 'bar_chart', component_property = 'figure')],
    [Input(component_id = 'demographic_metrics', component_property = 'value'),
    Input(component_id = 'prefecture_selection', component_property = 'value')]
)
def update_chart(metric_name, pref):
    chart_metric_header = html.H4(metric_name)

    #prepare data based on selection

    dff = df.copy()
    dff = dff[dff.Prefecture == pref][['City',metric_name]]

    #create bar chart
    fig = px.bar(
        data_frame = dff,
        x = dff.City,
        y = dff[metric_name],
        template = 'plotly_dark'
    )

    return chart_metric_header, fig


if __name__ == '__main__':

    #run app on localhost port 9999
    app.run_server(host='127.0.0.1',debug = True, port = '9999')