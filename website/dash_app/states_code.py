import os 
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from django_plotly_dash import DjangoDash
from dash.exceptions import PreventUpdate

#import for dash file
from website.dash_app import coronaAPI1 as capi
from website.dash_app import CoronaEDA2 as ceda
from website.dash_app import spare_file as sf


from flask import send_from_directory

app = DjangoDash('first', suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(style={"background-color":"rgb(17, 17, 17)"}, className='card', id='main-div', children=[
		html.Br(),
		html.Div(className='row flex', children=[
			html.Div(className='col-md-6', children=[
				dcc.Dropdown(id='dropdown-1', options=ceda.state_names_as_options, value="Maharashtra"),
		]),

		html.Div(className='col-md-6', children=[
			dcc.Dropdown(id='dropdown-2',
				options=[

				{'label': 'Confirmed Cases', 'value':'confirmed'},
				{'label': "Recovered Cases", 'value':'recovered'},
				{'label': "Deceased Cases",  'value':'deceased'},
				],
				value='confirmed',
			),
		])
	]),

	html.Div(style={"background-color":"rgb(17, 17, 17)"}, className='card', children=[
		dcc.Graph(id='cases_state', config={'displayModeBar':False}),	
	])
])
@app.callback(
	Output('cases_state', 'figure'),
	[Input('dropdown-1', 'value'),
	Input('dropdown-2', 'value')]
)
def figure1(state, status):
	return ceda.plot_trend_line(state, status)


app1 = DjangoDash('second', suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app1.layout = html.Div(style={"background-color":"rgb(17, 17, 17)"}, className='card', children=[
	html.Br(),
		html.Div(className='row flex', children=[
			html.Div(className='col-md-6', children=[
				dcc.Dropdown(id='dropdown-3', options=capi.state_names, value="Maharashtra"),
		]),

		html.Div(className='col-md-6', children=[
			dcc.Dropdown(id='dropdown-4',
				options=[

				{'label': 'Confirmed Cases', 'value':'confirmed'},
				{'label': "Recovered Cases", 'value':'recovered'},
				{'label': "Deceased Cases",  'value':'deceased'},
				{'label': "Active Cases",  'value':'active'},
				],
				value='confirmed',
			),
		])
	]),

	html.Div(style={"background-color":"rgb(17, 17, 17)"}, className='card', children=[
		dcc.Graph(id='overall_cases', config={'displayModeBar':False}),	
	])
])
@app1.callback(
	Output('overall_cases', 'figure'),
	[Input('dropdown-3', 'value'),
	 Input('dropdown-4', 'value')]
)
def figure2(state, status):
	return capi.bar_graph_overall(state, status)
 

app2 = DjangoDash('third', suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app2.layout = html.Div(style={"background-color":"rgb(17, 17, 17)"}, className='card', children=[
	html.Br(),
		html.Div(className='row flex', children=[
			html.Div(className='col-md-6', children=[
				dcc.Dropdown(id='dropdown-5', options=capi.state_names, value="Maharashtra"),
		]),

		html.Div(className='col-md-6', children=[
			dcc.Dropdown(id='dropdown-6',
				options=[
				{'label': 'Confirmed Cases', 'value':'confirmed'},
				{'label': "Recovered Cases", 'value':'recovered'},
				{'label': "Deceased Cases",  'value':'deceased'},
				],
				value='confirmed',
			),
		])
	]),

	html.Div(style={"background-color":"rgb(17, 17, 17)"}, className='card', children=[
		dcc.Graph(id='current_cases', config={'displayModeBar':False}),	
	])
])
@app2.callback(
	Output('current_cases', 'figure'),
	[Input('dropdown-5', 'value'),
	 Input('dropdown-6', 'value')]
)
def figure3(state, status):
	return capi.bar_graph_for_current(state, status)

#####################################################################
 
app3 = DjangoDash('state_vaccine_1')

app3.layout = html.Div(children=[
	html.Div(children=[
		dcc.Dropdown(id='dropdown-7', options=ceda.state_names_as_options, value='Maharashtra'),
	]),
	dcc.Graph(id='state_vaccine_1', config={'displayModeBar':False}),
])
@app3.callback(
	Output('state_vaccine_1', "figure"),
	[Input('dropdown-7', 'value')]
)
def figure4(state):
	return ceda.vaccine_administered(state)

#########################################################################

app4 = DjangoDash('state_vaccine_2')

app4.layout = html.Div(children=[
	html.Div(children=[
		dcc.Dropdown(id='dropdown-8', options=ceda.state_names_as_options, value='Maharashtra'),
	]),
	dcc.Graph(id='state_vaccine_2', config={'displayModeBar':False}),
])
@app4.callback(
	Output('state_vaccine_2', 'figure'),
	[Input('dropdown-8', 'value')]
)
def figure5(state):
	return ceda.vaccine_total_doses(state)

##############################################################################

app5 = DjangoDash('state_vaccine_3')

app5.layout = html.Div(style={'height':'600px'}, children=[
	html.Div(children=[
		dcc.Dropdown(id='dropdown-9', options=ceda.state_names_as_options, value='Maharashtra'),
	]),
	dcc.Graph(id='state_vaccine_3', config={'displayModeBar':False}),
])
@app5.callback(
	Output('state_vaccine_3', 'figure'),
	[Input('dropdown-9', 'value')]
)
def figure5(state):
	return ceda.aefi(state)


####################################################
app6 = DjangoDash('state_pie_india')

app6.layout = html.Div(children=[
	html.Div(children=[
		dcc.Dropdown(id='dropdown-10', options=ceda.state_names_as_options, value='Maharashtra'),
	]),
	dcc.Graph(id='state_vaccine_4', config={'displayModeBar':False}),
])
@app6.callback(
	Output('state_vaccine_4', 'figure'),
	[Input('dropdown-10', 'value')]
)
def figure5(state):
	return ceda.gender_dis(state)
