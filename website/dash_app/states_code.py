import os 
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

#import for dash file
from website.dash_app import coronaAPI1 as capi
from website.dash_app import CoronaEDA2 as ceda
from website.dash_app import spare_file as sf


from flask import send_from_directory

app = DjangoDash('first')

value = sf.sum(4, 5)

app.layout = html.Div(style={'color':'white'}, children=[
	html.H1("HEY"),
	html.H1(value)
	])

app9 = DjangoDash('second')


app9.layout = html.Div(style={'color':'white'}, children=[
	html.H1("HEY"),
	dcc.Graph(figure=ceda.vaccine_administered('India')),
])

app6 = DjangoDash('third')


app6.layout = html.Div(style={'color':'white'}, children=[
	html.H1("HEY"),
	dcc.Graph(figure=ceda.vaccine_total_doses('India')),
])


app7 = DjangoDash('fourth')


app7.layout = html.Div(style={'color':'white'}, children=[
	html.H1("HEY"),
	dcc.Graph(figure=ceda.aefi('India')),
])

