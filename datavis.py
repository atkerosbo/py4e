from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#df = pd.DataFrame({
#    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#    "Amount": [4, 1, 2, 2, 4, 5],
#    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
#})
df = pd.read_csv('Basket kod Baneta - Baza.csv')

dff = df.drop(
    labels=["Ime","SUM of Prisutnost","SUM of Odigrano","SUM of Pobeda","Calculated Field 2","Unnamed: 5","Unnamed: 6","Datum","Mesec"],
    axis = 1,
)
dff.rename(columns={'Ime.1':'Ime'}, inplace=True)

x=dff['Ime']
y=dff['Odigrano']
z=dff['Pobeda']

fig = px.bar(dff, x, y, color="Pobeda", barmode="stack")



app.layout = html.Div(children=[
    html.H1(children='Basket kod baneta'),

    html.Div(children='''
        Da vidimo ko kosi a ko vodu nosi.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)