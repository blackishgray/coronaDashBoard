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

from flask import send_from_directory

app1 = DjangoDash('india_plot')

###################################################################
#######figure 1 #################
app1.layout = html.Div(className='card', id='main-div', children=[
	
	html.Br(),

	html.Div(className='card', id='div1', style={'text-align': 'center'}, children=[

		html.H2(id='heading1', children=[
			"Vizualization of India based on specific conditions of COVID-19 Cases Reported."
			]),

		dcc.Dropdown(className='dropdown',id='dropdown-1',

			options=[
				{'label': 'Confirmed Cases', 'value':'confirmed'},
				{'label': "Recovered Cases", 'value': 'recovered'},
				{'label': "Deceased Cases",  'value': 'deaths'},
				{'label':'Active Cases', 	 'value':'active'},
			],
			value='confirmed',
			),
		html.Br(),
		dcc.Graph(id='india_map'),
		]),
])


@app1.callback(
	Output('india_map', 'figure'),
	[Input('dropdown-1', 'value')]
	)
def figure1(status):
	return capi.india_cases(status)

#################################################################
#########figure 2 #########################



app2 =  DjangoDash('total_cases_india_line_graph')

total_cases_india = ceda.total_cases_india()

app2.layout = html.Div(className='card', children=[
	html.Br(),

	html.Div(className='card', id='div1', style={'text-align': 'center'}, children=[

		html.H2(id='heading1', children=[
			"Trend line of total cases of COVID-19 reported in India"
			]),
		 
		html.Br(),
		dcc.Graph(figure=total_cases_india),
		]),
])

#########################################################
#################figure 3 ######################
app3 = DjangoDash('daily_cases')

app3.layout = html.Div(className='card', id='main-div1', children=[
	
	html.Br(),

	html.Div(className='card', id='div4', style={'text-align': 'center'}, children=[

		html.H2(id='heading3', children=[
			"Vizualization of India based on specific conditions of COVID-19 Cases Reported."
			]),

		dcc.Dropdown(className='dropdown',id='dropdown-2',

			options=[
				{'label': 'Confirmed Cases', 'value':'dailyconfirmed'},
				{'label': "Recovered Cases", 'value':'dailyrecovered'},
				{'label': "Deceased Cases",  'value':'dailydeceased'},
			],
			value='dailyconfirmed',
			),
		html.Br(),
		dcc.Graph(id='daily_count_cases'),
		]),
])
@app3.callback(
	Output('daily_count_cases', 'figure'),
	[Input('dropdown-2', 'value')]
	)
def figure3(status):
	return ceda.daily_count_cases_india(status)


#################################################
############figure 4##############
app4 = DjangoDash('recovry_death_india')

trend_lime_recovery_death = ceda.recovery_death_rate_india()

app4.layout = html.Div(children=[
	html.Br(),

	html.Div(className='card', id='div4', style={'text-align': 'center'}, children=[

		html.H2(id='heading1', children=[
			"Trend line of Recovery and Death Rate in India"
			]),
		 
		html.Br(),
		dcc.Graph(figure=trend_lime_recovery_death),
		]),
])