import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

import numpy as np

df = pd.read_csv('Basket kod Baneta - Baza.csv')

dff = df.drop(
    labels=["Ime","SUM of Prisutnost","SUM of Odigrano","SUM of Pobeda","Calculated Field 2","Unnamed: 5","Unnamed: 6","Datum","Mesec"],
    axis = 1,
)
dff.rename(columns={'Ime.1':'Ime'}, inplace=True)

x=dff['Ime']
y=dff['Odigrano']
z=dff['Pobeda']

# This dataframe has 244 lines, but 4 distinct values for `day`
#data_canada = px.data.gapminder().query("country == 'Canada'")


fig = px.bar(dff, x, z, color="Pobeda" , hover_data=['Pobeda', 'Odigrano'], title="Baket kod Baneta")

fig.show()