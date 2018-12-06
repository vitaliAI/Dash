import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
stock = 'TSLA'

df = web.DataReader(stock, 'yahoo', start, end)

print(df.head())

app.layout = html.Div(children=[
    html.H1('Stock Plotting'),
    dcc.Graph(id='example',
              figure={
                  'data': [
                      {'x': df.index , 'y': df.Close, 'type': 'line', 'name': 'boats'},
                  ],
                  'layout': {
                      'title': f'{stock} Daily Close'
                  }
              })
])


if __name__ == '__main__':
    app.run_server(debug=True)