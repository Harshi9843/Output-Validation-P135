import pandas as pd 
import plotly.express as px

df = pd.read_csv("star_with_gravity.csv")

star_name = df["Star_name"].tolist()
mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
distance = df["Distance"].tolist()
gravity = df["Gravity"].tolist()

fig = px.bar(x=star_name, y = mass)
fig.show()

fig2 = px.bar(x=star_name, y=radius)
fig2.show()

fig3 = px.bar(x=star_name, y=distance)
fig3.show()

fig4 = px.bar(x=star_name, y=gravity)
fig4.show()
