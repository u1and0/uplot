#!/usr/bin/env python3
import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # File upload bunner
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Drag and Drop or ',
                           html.A('Select Files')]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True),
    html.Div(id='the_graph'),
    html.Div(id='output-data-upload'),
])


def plot_graph(df, filename):
    data = [
        go.Scatter(
            x=df.index,
            y=df.T.values[_],
        ) for _ in range(len(df.columns))
    ]
    layout = go.Layout(xaxis={
        'type': 'linear',
        'title': df.index.name
    },
                       title=go.layout.Title(text=filename),
                       yaxis={'title': df.columns[0]},
                       margin={
                           'l': 40,
                           'b': 50
                       },
                       hovermode='closest')
    return dcc.Graph(id='the_graph', figure={'data': data, 'layout': layout})


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), index_col=0)
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        # dft = df.T
        print(df.index)
        print(df.T.values[0])
    except Exception as e:
        print(e)
        return html.Div(['There was an error processing this file.'])

    return html.Div([
        # Plot graph
        plot_graph(df, filename),
        # ---graph ^
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),
        dash_table.DataTable(data=df.to_dict('records'),
                             columns=[{
                                 'name': i,
                                 'id': i
                             } for i in df.columns]),
        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...',
                 style={
                     'whiteSpace': 'pre-wrap',
                     'wordBreak': 'break-all'
                 })
    ])


@app.callback(
    Output(
        'output-data-upload',
        'children',
    ), [Input('upload-data', 'contents')],
    [State('upload-data', 'filename'),
     State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d)
            for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8888)
