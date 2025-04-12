from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table
import plotly.express as px

df = pd.read_csv('Student_Performance_data.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
myText = dcc.Markdown(children = '')
myInput = dcc.Input(id='my-input', value='Enter some text', type='text')

app.layout = dbc.Container([myText, myInput])

@app.callback(
    Output(myText, component_property='children'),
    Input(myInput, component_property='value')
)

def update_output(user_input):
    return user_input

if __name__ == '__main__':
 app.run(debug=True) 