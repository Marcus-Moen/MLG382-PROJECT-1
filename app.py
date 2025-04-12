from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import joblib

# Load your data and trained model
df = pd.read_csv('Student_Performance_data.csv')
# model = joblib.load('your_model.pkl')  # Replace with your actual model file

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[
    dbc.themes.SOLAR,
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap"
])

# Layout of the Dash app
app.layout = dbc.Container([
    html.Br(),

    dcc.Markdown('# **BrightPath Academy - Student Performance Dashboard**',
                 style={'textAlign': 'center', 'fontSize': 30, 'color': 'white', 'fontFamily': 'Poppins, sans-serif'}),

    html.Hr(),
    html.Br(),

    dcc.Markdown('## **Predict Student Grade Class**',
                 style={'textAlign': 'center', 'fontSize': 24, 'color': 'white', 'fontFamily': 'Poppins, sans-serif'}),

    html.Br(),

dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Enter Student Info", className="text-center text-white",
                               style={'fontSize': '20px', 'fontWeight': 'bold'}),

                dbc.CardBody([

                    dbc.Label("Weekly Study Time (hours)", style={'color': 'white'}),
                    dcc.Input(id="input-studytime", type="number", min=0, step=1, value=10,
                              style={'width': '100%', 'marginBottom': '15px'}),
                    
                    dbc.Label("Days Absent", style={'color': 'white'}),
                    dcc.Input(id="input-absences", type="number", min=0, step=1, value=5,
                              style={'width': '100%', 'marginBottom': '15px'}),
                    
                    dbc.Label(["Parental Support ",
                               dbc.Badge("?", id="tooltip-parental", color="info", className="ms-1")],
                              style={'color': 'white'}),
                    dcc.Dropdown(['Yes', 'No'], 'Yes', id='input-parental',
                                 style={'width': '100%', 'marginBottom': '15px'}),

                    dbc.Label(["Tutoring ",
                               dbc.Badge("?", id="tooltip-tutoring", color="info", className="ms-1")],
                              style={'color': 'white'}),
                    dcc.Dropdown(['Yes', 'No'], 'No', id='input-tutoring',
                                 style={'width': '100%', 'marginBottom': '15px'}),

                    dbc.Label(["Extracurricular ",
                               dbc.Badge("?", id="tooltip-extra", color="info", className="ms-1")],
                              style={'color': 'white'}),
                    dcc.Dropdown(['Yes', 'No'], 'Yes', id='input-extra',
                                 style={'width': '100%', 'marginBottom': '25px'}),

                    dbc.Button("🎯 Predict Grade Class", id='predict-button', color='primary',
                               style={
                                   'width': '100%',
                                   'boxShadow': '0 4px 6px rgba(0,0,0,0.3)',
                                   'fontWeight': 'bold'
                               }),

                    html.Br(), html.Br(),

                    html.Div(id='prediction-output', style={
                        'fontSize': 26,
                        'color': '#FFD700',
                        'textAlign': 'center',
                        'transition': 'all 0.3s ease-in-out',
                        'fontFamily': 'Poppins, sans-serif'
                    }),
                ])
            ], color="dark", inverse=True, style={
                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.4)",
                "borderRadius": "15px",
                "padding": "20px"
            })
        ], width=6)
    ], justify='center'),

        html.Br(), html.Br(),

        html.Footer("© 2025 BrightPath Academy", style={
        'textAlign': 'center',
        'color': 'white',
        'fontSize': '14px',
        'fontFamily': 'Poppins, sans-serif',
        'marginTop': '50px'
    })

], fluid=True, style={
    'background': 'linear-gradient(to right, #0f2027, #203a43, #2c5364)',
    'minHeight': '100vh',
    'padding': '20px'})


app.layout.children.append(
    dbc.Tooltip("Does the student receive help from parents with schoolwork?",
                target="tooltip-parental", placement='right', style={'fontSize': '14px'})
)
app.layout.children.append(
    dbc.Tooltip("Is the student enrolled in extra tutoring sessions?",
                target="tooltip-tutoring", placement='right', style={'fontSize': '14px'})
)
app.layout.children.append(
    dbc.Tooltip("Is the student involved in extracurricular activities?",
                target="tooltip-extra", placement='right', style={'fontSize': '14px'})
)


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