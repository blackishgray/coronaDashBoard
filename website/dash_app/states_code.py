import os 
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from dash.exceptions import PreventUpdate

#import for dash file
from website.dash_app import coronaAPI1 as capi
from website.dash_app import CoronaEDA2 as ceda
from website.dash_app import spare_file as sf


from flask import send_from_directory

# app = DjangoDash('first')

# app.layout = html.Div(style={'color':'white'}, children=[
# 	html.H1("HEY"),
# 	dcc.Input(type='text', id='inp1'),
# 	dcc.Input(type='text', id='inp2'),
# 	html.H2(style={'background-color':'white', 'color':'black', 'width':'50px', "height":'60px'}, id='out')
# 	])
# @app.callback(
# 	Output('out', 'children'),
# 	[Input('inp1', 'value'),
# 	Input('inp2', 'value')]
# 	)
# def update(a, b):
# 	if a == "None" or b == "None":
# 		raise PreventUpdate
# 	else:
# 		return sf.sum(int(a), int(b))


app = DjangoDash('first')


app.layout = html.Div(children=[
	dcc.Input(type="text", id='inp'),
	dcc.Graph(id='graph1', config={'displayModeBar':False}),
])

app.callback(
	Output('graph1', 'figure'),
	[Input('inp', 'value')]
	)
def update_graph(state):
	if state == None:
		state='Maharashtra'
	return ceda.vaccine_total_doses(state)