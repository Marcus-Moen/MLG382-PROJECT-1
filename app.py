from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import joblib

# Load your data and trained model
df = pd.read_csv('Student_Performance_data.csv')
model = joblib.load('model.joblib')  # Replace with your actual model file

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[
    dbc.themes.SOLAR,
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap"
])

# This if for Render
server = app.server

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
                        dbc.Label(["Age ", dbc.Badge("?", id="tooltip-age", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Input(id="input-age", type="number", min=10, max=25, value=17, style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Gender ", dbc.Badge("?", id="tooltip-gender", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Dropdown(['Male', 'Female'], 'Male', id='input-gender', style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Ethnicity ", dbc.Badge("?", id="tooltip-ethnicity", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Dropdown(['Caucasian', 'African American', 'Asian', 'Other'], 'Ethnicity', id='input-ethnicity', style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Parental Education Level ", dbc.Badge("?", id="tooltip-parentaledu", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Dropdown(['None', 'Primary', 'Secondary', 'Tertiary'], 'Secondary', id='input-parentaledu', style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Weekly Study Time (hours) ", dbc.Badge("?", id="tooltip-studytime", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Input(id="input-studytime", type="number", min=0, step=1, value=10, style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Days Absent ", dbc.Badge("?", id="tooltip-absences", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Input(id="input-absences", type="number", min=0, step=1, value=5, style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Tutoring ", dbc.Badge("?", id="tooltip-tutoring", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Dropdown(['Yes', 'No'], 'No', id='input-tutoring', style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Parental Support Level ", dbc.Badge("?", id="tooltip-parental", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Dropdown([0, 1, 2, 3], 2, id='input-parental', style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Sports Participation ", dbc.Badge("?", id="tooltip-sports", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Dropdown(['Yes', 'No'], 'No', id='input-sports', style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Music Participation ", dbc.Badge("?", id="tooltip-music", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Dropdown(['Yes', 'No'], 'Yes', id='input-music', style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Volunteering ", dbc.Badge("?", id="tooltip-volunteering", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Dropdown(['Yes', 'No'], 'No', id='input-volunteering', style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Total Extracurricular Activities ", dbc.Badge("?", id="tooltip-total-extra", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Input(id="input-total-extra", type="number", min=0, step=1, value=1, style={'width': '100%', 'marginBottom': '15px', 'color': 'black'}),

                        dbc.Label(["Parental Education Support ", dbc.Badge("?", id="tooltip-parentaledusupport", color="info", className="ms-1")], style={'color': 'white'}),
                        dcc.Input(id="input-parentaledusupport", type="number", min=0, step=1, value=4, style={'width': '100%', 'marginBottom': '25px', 'color': 'black'}),

                    dbc.Button("🎯 Predict Grade Class", id='predict-button', color='primary',
                               style={
                                   'width': '100%',
                                   'boxShadow': '0 4px 6px rgba(0,0,0,0.3)',
                                   'fontWeight': 'bold'
                               }),

                    html.Br(), html.Br(),

                    html.Div(id='prediction-output', style={
                        'fontSize': 26,
                        'color': '#FFFFED',
                        'fontWeight': 'bold',
                        'textAlign': 'center',
                        'transition': 'all 0.5s ease-in-out',
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


app.layout.children.append(dbc.Tooltip("Enter the student's age (10–25 years old).", target="tooltip-age", placement='right'))
app.layout.children.append(dbc.Tooltip("Select the student's gender identity.", target="tooltip-gender", placement='right'))
app.layout.children.append(dbc.Tooltip("Choose the student's ethnicity or cultural background.", target="tooltip-ethnicity", placement='right'))
app.layout.children.append(dbc.Tooltip("Highest level of education completed by either parent.", target="tooltip-parentaledu", placement='right'))
app.layout.children.append(dbc.Tooltip("Total weekly hours spent studying outside of class.", target="tooltip-studytime", placement='right'))
app.layout.children.append(dbc.Tooltip("Number of school days the student has missed.", target="tooltip-absences", placement='right'))
app.layout.children.append(dbc.Tooltip("Is the student receiving extra academic tutoring?", target="tooltip-tutoring", placement='right'))
app.layout.children.append(dbc.Tooltip("Scale from 0–3 indicating parental involvement/support.", target="tooltip-parental", placement='right'))
app.layout.children.append(dbc.Tooltip("Is the student involved in sports activities?", target="tooltip-sports", placement='right'))
app.layout.children.append(dbc.Tooltip("Is the student participating in any music-related activities?", target="tooltip-music", placement='right'))
app.layout.children.append(dbc.Tooltip("Is the student engaged in volunteering work?", target="tooltip-volunteering", placement='right'))
app.layout.children.append(dbc.Tooltip("Number of extracurricular activities the student participates in.", target="tooltip-total-extra", placement='right'))
app.layout.children.append(dbc.Tooltip("How much support is provided by parents toward the student’s education.", target="tooltip-parentaledusupport", placement='right'))



@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-button', 'n_clicks'),
    State('input-age', 'value'),
    State('input-gender', 'value'),
    State('input-ethnicity', 'value'),
    State('input-parentaledu', 'value'),
    State('input-studytime', 'value'),
    State('input-absences', 'value'),
    State('input-tutoring', 'value'),
    State('input-parental', 'value'),
    State('input-sports', 'value'),
    State('input-music', 'value'),
    State('input-volunteering', 'value'),
    State('input-total-extra', 'value'),
    State('input-parentaledusupport', 'value'),
)

def predict_grade(n_clicks, age, gender, ethnicity, parental_edu, study, absences, tutoring, parental_support,
                  sports, music, volunteering, total_extra, parental_edu_support):
    if n_clicks is None:
        return ""

    # Encode categorical values based on your training set
    gender = 1 if gender == 'Male' else 0

    ethnicity_mapping = {'Caucasian': 0, 'African American': 1, 'Asian': 2, 'Other': 3}
    ethnicity = ethnicity_mapping.get(ethnicity, 0)

    edu_mapping = {'None': 0, 'Primary': 1, 'Secondary': 2, 'Tertiary': 3}
    parental_edu = edu_mapping.get(parental_edu, 2)

    tutoring = 1 if tutoring == 'Yes' else 0
    sports = 1 if sports == 'Yes' else 0
    music = 1 if music == 'Yes' else 0
    volunteering = 1 if volunteering == 'Yes' else 0

    # Create the input data using the actual user input
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Ethnicity': [ethnicity],
        'ParentalEducation': [parental_edu],
        'StudyTimeWeekly': [study],
        'Absences': [absences],
        'Tutoring': [tutoring],
        'ParentalSupport': [parental_support],
        'Sports': [sports],
        'Music': [music],
        'Volunteering': [volunteering],
        'TotalExtracurricular': [total_extra],
        'ParentalEduSupport': [parental_edu_support],
    })

    # Ensure the model expects this DataFrame format. If the model expects a numpy array, convert it.
    prediction = model.predict(input_data)[0]

    return f'Predicted Grade Class: {prediction}'


# To run the app 

if __name__ == "__main__":
    app.run(debug=True)
