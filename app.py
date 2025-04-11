from dash import Dash, html
import pandas as pd
from dash import dash_table

df = pd.read_csv('Student_Performance_data.csv')

app = Dash()

app.layout = [
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
]

if __name__ == '__main__':
 app.run(debug=True)