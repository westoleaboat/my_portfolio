import plotly.express as px
import pandas as pd

data = pd.read_csv('methane_hist_emissions.csv')

fig = px.scatter(data)

fig.show()

