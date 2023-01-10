import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

import numpy as np
#Importing and cleaning the data
df = pd.read_csv("F:\WORK\py4e\BasketkodBaneta.csv")


#the values
x=df['Ime']
y=df['Broj odigranih basketa']
z=df['Broj pobeda']

# the funcion
fig = px.bar(df, x, z,
             hover_data=['Broj pobeda', 'Broj odigranih basketa'], color='Broj pobeda',
             labels={'Broj pobeda':'Broj pobeda od ukupno odigranih meceva'}, height=400)
fig.show()