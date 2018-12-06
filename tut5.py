import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import colorlover as cl

colorscale = cl.scales['9']['qual']['Paired']

app = dash.Dash()

app.layout = html.Div(children=[

    html.Div(children='''
        Symbol to Graph:
    '''),

    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')

])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_graph(input_data):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'yahoo', start, end)

    return dcc.Graph(id='example',
              figure={
                  'data': [
                      {'x': df.index,
                       'open': df['Open'],
                       'high': df['High'],
                       'low': df['Low'],
                       'close': df['Close'],
                       'type': 'candlestick',
                       'name': input_data,
                       'legendgroup': input_data,
                       'increasing': {'line': {'color': 'green'}},
                       'decreasing': {'line': {'color': 'red'}}
                       }
                  ],
                  'layout': {
                      'title': f'{input_data.upper()} Daily Close'
                  }
              })


if __name__ == '__main__':
    app.run_server(debug=True)