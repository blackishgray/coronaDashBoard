import os 
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

from django_plotly_dash import DjangoDash

#import for dash file
from website.dash_app import coronaAPI1 as capi
from website.dash_app import CoronaEDA2 as ceda

from flask import send_from_directory

external_stylesheets =  r'C:/Users/Ratnadeep Gawade/Desktop/python/django/coronaApp/app/website/assets/style.css'

app1 = DjangoDash('india_plot', suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets])

###################################################################
#######figure 1 #################
app1.layout = html.Div(id='main-div', children=[

	html.Br(),

		dcc.Dropdown(className='dropdown',id='dropdown-1',
			style={'width':'200px'},
			options=[
				{'label': 'Confirmed Cases', 'value':'confirmed'},
				{'label': "Recovered Cases", 'value': 'recovered'},
				{'label': "Deceased Cases",  'value': 'deaths'},
				{'label':'Active Cases', 	 'value':'active'},
			],
			value='confirmed',
			),
		html.Br(),
		html.Div(children=[
			dcc.Graph(id='india_map', config={'displayModeBar':False}),
		]),
])

@app1.callback(
	Output('india_map', 'figure'),
	[Input('dropdown-1', 'value')]
	)
def figure1(status):
	return capi.india_cases(status)

# #################################################################
# #########figure 2 #########################



app2 = DjangoDash('total_cases_india_line_graph', external_stylesheets=[external_stylesheets])

app2.layout = html.Div(children=[
	html.Br(),

	html.Div(className='card', id='div2', children=[

		html.Br(),
		dcc.Graph(figure=ceda.total_cases_india(), config={'displayModeBar':False}),
		]),
])

# #########################################################
# #################figure 3 ######################
app3 = DjangoDash('daily_cases', external_stylesheets=[external_stylesheets])

app3.layout = html.Div(children=[

	html.Br(),

	html.Div(children=[

		dcc.Dropdown(className='dropdown',id='dropdown-2', 
			style={'width':'200px'},
			options=[
				{'label': 'Confirmed Cases', 'value':'dailyconfirmed'},
				{'label': "Recovered Cases", 'value':'dailyrecovered'},
				{'label': "Deceased Cases",  'value':'dailydeceased'},
			],
			value='dailyconfirmed',
			placeholder='Select a status you want to vizualize..'
			),
		html.Br(),
		dcc.Graph(id='daily_count_cases', config={'displayModeBar':False}),
		]),
])
@app3.callback(
	Output('daily_count_cases', 'figure'),
	[Input('dropdown-2', 'value')]
	)
def figure3(status):
	return ceda.daily_count_cases_india(status)


app4 = DjangoDash('first', suppress_callback_exceptions=True)

app4.layout = html.Div(children=[
		html.Br(),
		html.Div(className='row', children=[
			html.Div(className='six columns', children=[
				dcc.Dropdown(id='dropdown-1', options=ceda.state_names_as_options, value="Maharashtra"),
		], style=dict(width='50%')),

		html.Div(className='col-md-6', children=[
			dcc.Dropdown(id='dropdown-2',
				options=[

				{'label': 'Confirmed Cases', 'value':'confirmed'},
				{'label': "Recovered Cases", 'value':'recovered'},
				{'label': "Deceased Cases",  'value':'deceased'},
				],
				value='confirmed',
			),
		], style=dict(width='50%', float='right'))
	], style=dict(display='flex')),

	html.Div(className='card', children=[
		dcc.Graph(id='cases_state', config={'displayModeBar':False}),	
	])
])
@app4.callback(
	Output('cases_state', 'figure'),
	[Input('dropdown-1', 'value'),
	Input('dropdown-2', 'value')]
)
def figure1(state, status):
	return ceda.plot_trend_line(state, status)


app5 = DjangoDash('second', suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets])

app5.layout = html.Div(children=[
	html.Br(),
		html.Div(className='row', children=[
			html.Div(className='col-md-6', children=[
				dcc.Dropdown(id='dropdown-3', options=capi.state_names, value="Maharashtra"),
		], style=dict(width='50%')),

		html.Div(className='col-md-3', children=[
			dcc.Dropdown(id='dropdown-4',
				options=[

				{'label': 'Confirmed Cases', 'value':'confirmed'},
				{'label': "Recovered Cases", 'value':'recovered'},
				{'label': "Deceased Cases",  'value':'deceased'},
				{'label': "Active Cases",  'value':'active'},
				],
				value='confirmed',
			),
		], style=dict(width='50%'))
	], style=dict(display='flex')),

	html.Div(className='card', children=[
		dcc.Graph(id='overall_cases', config={'displayModeBar':False}),	
	])
])
@app5.callback(
	Output('overall_cases', 'figure'),
	[Input('dropdown-3', 'value'),
	 Input('dropdown-4', 'value')]
)
def figure2(state, status):
	return capi.bar_graph_overall(state, status)
 

app6 = DjangoDash('third', suppress_callback_exceptions=True)

app6.layout = html.Div(children=[
	html.Br(),
		html.Div(className='row', children=[
			html.Div(className='col-md-6', children=[
				dcc.Dropdown(id='dropdown-5', options=capi.state_names, value="Maharashtra"),
		], style=dict(width='50%')),

		html.Div(className='col-md-6', children=[
			dcc.Dropdown(id='dropdown-6',
				options=[
				{'label': 'Confirmed Cases', 'value':'confirmed'},
				{'label': "Recovered Cases", 'value':'recovered'},
				{'label': "Deceased Cases",  'value':'deceased'},
				],
				value='confirmed',
			),
		], style=dict(width='50%'))
	], style=dict(display='flex')),

	html.Div(className='card', children=[
		dcc.Graph(id='current_cases', config={'displayModeBar':False}),	
	], style=dict(backgroundColor='rgba(17 , 17, 17, 1)'))
])
@app6.callback(
	Output('current_cases', 'figure'),
	[Input('dropdown-5', 'value'),
	 Input('dropdown-6', 'value')]
)
def figure3(state, status):
	return capi.bar_graph_for_current(state, status)



app7 = DjangoDash('district_wise_cases', suppress_callback_exceptions=True)

app7.layout = html.Div( children=[
	html.Br(),
		html.Div(className='row flex', children=[
			html.Div(className='col-md-6', children=[
				dcc.Dropdown(id='dropdown-7', options=ceda.state_names_as_options, value="Maharashtra"),
		], style=dict(width='50%')),

		html.Div(className='col-md-6', children=[
			dcc.Dropdown(id='dropdown-8', options=[], value='Mumbai'),
		], style=dict(width='50%')),
	], style=dict(display='flex')),

	html.Div(className='card', children=[
		dcc.Graph(id='district_cases', config={'displayModeBar':False}),	
	])
])
@app7.callback(
	Output('dropdown-8', 'options'),
	 [Input('dropdown-7', 'value')]
)
def figure3(state):
	return ceda.cities_of_state(state)

@app7.callback(
	Output('district_cases', 'figure'),
	[Input('dropdown-7', 'value'),
	 Input('dropdown-8', 'value')]
)
def figure3(state, district):
	return ceda.district_wise_cases(state, district)