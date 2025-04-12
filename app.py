from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import joblib

# Load your data and trained model
df = pd.read_csv('Student_Performance_data.csv')
# model = joblib.load('your_model.pkl')  # Replace with your actual model file

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

# Layout of the Dash app
app.layout = dbc.Container([
    html.Br(),

    dcc.Markdown('# **BrightPath Academy - Student Performance Dashboard**',
                 style={'textAlign': 'center', 'fontSize': 30, 'color': 'white'}),

    html.Hr(),
    html.Br(),

    dcc.Markdown('## **Predict Student Grade Class**',
                 style={'textAlign': 'center', 'fontSize': 24, 'color': 'white'}),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Label("Weekly study time in hours", style={'color': 'white'}),
            dcc.Input(id="input-studytime", type="number", min=0, step=1, value=10, style={'width': '100%'}),
            html.Br(), html.Br(),

            dbc.Label("Number of days Absent", style={'color': 'white'}),
            dcc.Input(id="input-absences", type="number", min=0, step=1, value=5, style={'width': '100%'}),
            html.Br(), html.Br(),

            dbc.Label("Parental Support", style={'color': 'white'}),
            dcc.Dropdown(['Yes', 'No'], 'Yes', id='input-parental', style={'width': '100%'}),
            html.Br(), html.Br(),

            dbc.Label("Tutoring", style={'color': 'white'}),
            dcc.Dropdown(['Yes', 'No'], 'No', id='input-tutoring', style={'width': '100%'}),
            html.Br(), html.Br(),

            dbc.Label("Extracurricular", style={'color': 'white'}),
            dcc.Dropdown(['Yes', 'No'], 'Yes', id='input-extra', style={'width': '100%'}),
            html.Br(), html.Br(),

            dbc.Button("Predict Grade Class", id='predict-button', color='primary', style={'width': '100%'}),
            html.Br(), html.Br(),

            html.Div(id='prediction-output', style={
                'fontSize': 24,
                'color': 'white',
                'textAlign': 'center'
            }),
        ], width=6)
    ], justify='center'),

], fluid=True)


@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-button', 'n_clicks'),
    State('input-studytime', 'value'),
    State('input-absences', 'value'),
    State('input-parental', 'value'),
    State('input-tutoring', 'value'),
    State('input-extra', 'value'),
)
def predict_grade(n_clicks, study, absences, parental, tutoring, extra):
    if n_clicks is None:
        return ""
    
    parental_support = 1 if parental == 'Yes' else 0
    tutoring_support = 1 if tutoring == 'Yes' else 0
    extracurricular = 1 if extra == 'Yes' else 0

    input_data = np.array([[study, absences, parental_support, tutoring_support, extracurricular]])
    prediction = model.predict(input_data)[0]

    return f'🎓 Predicted Grade Class: **{prediction}**'


# To run the app 

if __name__ == '__main__':
 app.run(debug=True) 