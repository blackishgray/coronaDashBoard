import os 
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

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



app = DjangoDash('first', suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(style={'background-color':'rgba(17, 17, 17)'}, children=[

	html.Br(),

	html.Div(id='row flex', style={'text-align': 'center'}, children=[

		html.Div(className='row flex', children=[ 

			html.Div(className='col-md-6', children=[

				dcc.Dropdown(id='dropdown-1', options=ceda.state_names_as_options, value='Maharashtra'),

				]),

			html.Div(className='col-md-6', children=[
				dcc.Dropdown(className='dropdown',id='dropdown-2', 
					# style={'width':'200px'},
					options=[
					{'label': 'Confirmed Cases', 'value':'confirmed'},
					{'label': "Recovered Cases", 'value':'recovered'},
					{'label': "Deceased Cases",  'value':'deceased'},
					],
					value='confirmed',
					placeholder='Select a status you want to vizualize..'
					),
				html.Br(),
				]),
			]),


		]),
	html.Div(className='card', children=[

		dcc.Graph(id='daily_count_cases', config={'displayModeBar':False}),

		]),

])
@app.callback(
	Output('daily_count_cases', 'figure'),
	[Input('dropdown-1', 'value'),
	Input('dropdown-2', 'value')],
	)
def figure1(state, status):
	return ceda.plot_trend_line(state, status)

app2 = DjangoDash('second', suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app2.layout = html.Div(style={'background-color':'rgba(17, 17, 17)'}, children=[

	html.Br(),

	html.Div(id='row flex', style={'text-align': 'center'}, children=[

		html.Div(className='row flex', children=[ 

			html.Div(className='col-md-6', children=[

				dcc.Dropdown(id='dropdown-1', options=capi.state_names, value='Maharashtra'),

				]),

			html.Div(className='col-md-6', children=[
				dcc.Dropdown(className='dropdown',id='dropdown-2', 
					# style={'width':'200px'},
					options=[
					{'label': 'Confirmed Cases', 'value':'confirmed'},
					{'label': "Recovered Cases", 'value':'recovered'},
					{'label': "Deceased Cases",  'value':'deceased'},
					],
					value='confirmed',
					placeholder='Select a status you want to vizualize..'
					),
				html.Br(),
				]),
			]),


		]),
	html.Div(className='card', children=[

		dcc.Graph(id='current_cases', config={'displayModeBar':False}),

		]),

])
@app2.callback(
	Output('current_cases', 'figure'),
	[Input('dropdown-1', 'value'),
	Input('dropdown-2', 'value')],
	)
def figure2(state, status):
	return capi.bar_graph_for_current(state, status)


app3 = DjangoDash('third', suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app3.layout = html.Div(style={'background-color':'rgba(17, 17, 17)'}, children=[

	html.Br(),

	html.Div(id='row flex', style={'text-align': 'center'}, children=[

		html.Div(className='row flex', children=[ 

			html.Div(className='col-md-6', children=[

				dcc.Dropdown(id='dropdown-1', options=capi.state_names, value='Maharashtra'),

				]),

			html.Div(className='col-md-6', children=[
				dcc.Dropdown(className='dropdown',id='dropdown-2', 
					# style={'width':'200px'},
					options=[
					{'label': 'Confirmed Cases', 'value':'confirmed'},
					{'label': "Recovered Cases", 'value':'recovered'},
					{'label': "Deceased Cases",  'value':'deceased'},
					],
					value='confirmed',
					placeholder='Select a status you want to vizualize..'
					),
				html.Br(),
				]),
			]),


		]),
	html.Div(className='card', children=[

		dcc.Graph(id='overall_cases', config={'displayModeBar':False}),

		]),

])
@app3.callback(
	Output('overall_cases', 'figure'),
	[Input('dropdown-1', 'value'),
	Input('dropdown-2', 'value')],
	)
def figure3(state, status):
	return capi.bar_graph_overall(state, status)














# app = DjangoDash('first', suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app.layout = html.Div(style={"background-color":"rgb(17, 17, 17)"}, children=[
# 	dcc.Dropdown(id='dropdown-1', options=ceda.state_names_as_options, value='Maharashtra'),
# 	html.H1(id='out', style={"background-color":"white"}),

# 	html.Br((), 
# 	dcc.Dropdown(id='cities', options=[]),

# 	html.H1(id='out2', style={"background-color":"white"})

# 	dcc.Graph(id='cases_line')

# ])

# @app.callback(
# 	Output('cities', 'options'),
# 	Input('dropdown-1', 'value')
# 	)
# def cities_values(state):
# 	return ceda.cities_of_state(state)