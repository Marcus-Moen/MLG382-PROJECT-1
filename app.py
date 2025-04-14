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

            # UI additions 
                        dbc.Label("Age", style={'color': 'white'}),
                        dcc.Input(id="input-age", type="number", min=10, max=25, value=17, style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Gender", style={'color': 'white'}),
                        dcc.Dropdown(['Male', 'Female'], 'Male', id='input-gender', style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Ethnicity", style={'color': 'white'}),
                        dcc.Dropdown(['Group A', 'Group B', 'Group C', 'Group D', 'Group E'], 'Group A', id='input-ethnicity', style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Parental Education Level", style={'color': 'white'}),
                        dcc.Dropdown(['None', 'Primary', 'Secondary', 'Tertiary'], 'Secondary', id='input-parentaledu', style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Weekly Study Time (hours)", style={'color': 'white'}),
                        dcc.Input(id="input-studytime", type="number", min=0, step=1, value=10, style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Days Absent", style={'color': 'white'}),
                        dcc.Input(id="input-absences", type="number", min=0, step=1, value=5, style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Tutoring", style={'color': 'white'}),
                        dcc.Dropdown(['Yes', 'No'], 'No', id='input-tutoring', style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Parental Support Level", style={'color': 'white'}),
                        dcc.Dropdown([0, 1, 2, 3], 2, id='input-parental', style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Sports Participation", style={'color': 'white'}),
                        dcc.Dropdown(['Yes', 'No'], 'No', id='input-sports', style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Music Participation", style={'color': 'white'}),
                        dcc.Dropdown(['Yes', 'No'], 'Yes', id='input-music', style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Volunteering", style={'color': 'white'}),
                        dcc.Dropdown(['Yes', 'No'], 'No', id='input-volunteering', style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Total Extracurricular Activities", style={'color': 'white'}),
                        dcc.Input(id="input-total-extra", type="number", min=0, step=1, value=1, style={'width': '100%', 'marginBottom': '15px'}),

                        dbc.Label("Parental Education Support", style={'color': 'white'}),
                        dcc.Input(id="input-parentaledusupport", type="number", min=0, step=1, value=4, style={'width': '100%', 'marginBottom': '25px'}),


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


# app.layout.children.append(
#     dbc.Tooltip("Does the student receive help from parents with schoolwork?",
#                 target="tooltip-parental", placement='right', style={'fontSize': '14px'})
# )
# app.layout.children.append(
#     dbc.Tooltip("Is the student enrolled in extra tutoring sessions?",
#                 target="tooltip-tutoring", placement='right', style={'fontSize': '14px'})
# )
# app.layout.children.append(
#     dbc.Tooltip("Is the student involved in extracurricular activities?",
#                 target="tooltip-extra", placement='right', style={'fontSize': '14px'})
# )


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

    ethnicity_mapping = {'Group A': 0, 'Group B': 1, 'Group C': 2, 'Group D': 3, 'Group E': 4}
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

    return f'🎓 Predicted Grade Class: **{prediction}**'


# To run the app 

if __name__ == '__main__':
 app.run(debug=True) 