import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('C:/Users/DELL/Documents/Kuliah/Semester 4/PBO/PBO_Lanjut/PBOLanjut_Pertemuan12/Praktikum/data.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Create a bar chart using Plotly Express with different colors for each category
fig = px.bar(df, x='Category', y='Value', color='Category', title='Sample Bar Chart with Different Colors')

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Dash Data Visualization'),

    dcc.Markdown('''
        ### Markdown Example

        This is an example of Markdown in Dash.

        - You can create lists
        - Use **bold** text
        - Add [links](https://plotly.com/dash/)

        Here is the bar chart below:
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)