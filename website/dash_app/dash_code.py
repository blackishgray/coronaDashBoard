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

app1 = DjangoDash('india_plot', suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

###################################################################
#######figure 1 #################
app1.layout = html.Div(style={'background-color':'rgba(17, 17, 17, 1)', 'height':'540px'}, id='main-div', children=[

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
		html.Div(style={'background-color':'rgba(17, 17, 17, 1)'}, className='card', children=[
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



app2 = DjangoDash('total_cases_india_line_graph')

app2.layout = html.Div(className='card', children=[
	html.Br(),

	html.Div(className='card', id='div2', children=[

		html.Br(),
		dcc.Graph(figure=ceda.total_cases_india(), config={'displayModeBar':False}),
		]),
])

# #########################################################
# #################figure 3 ######################
app3 = DjangoDash('daily_cases')

app3.layout = html.Div(className='card', id='main-div1', children=[

	html.Br(),

	html.Div(className='card', id='div3', style={'text-align': 'center'}, children=[

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


# #################################################
# ############figure 4##############
app4 = DjangoDash('recovry_death_india')

app4.layout = html.Div(children=[
	html.Br(),

	html.Div(className='card', id='div4', style={'text-align': 'center'}, children=[

		html.Br(),
		dcc.Graph(figure=ceda.recovery_death_rate_india(), config={'displayModeBar':False}),
		]),
])


app5 = DjangoDash('vaccine_1')

app5.layout = html.Div(children=[
	dcc.Graph(figure=ceda.vaccine_administered('India'), config={'displayModeBar':False}),
])


app6 = DjangoDash('vaccine_2')

app6.layout = html.Div(children=[
	dcc.Graph(figure=ceda.vaccine_total_doses('India'), config={'displayModeBar':False}),
])


app7 = DjangoDash('vaccine_3')

app7.layout = html.Div(style={'height':'600px'}, children=[
	dcc.Graph(figure=ceda.aefi('India'), config={'displayModeBar':False}),
])


app8 = DjangoDash('pie_india')

app8.layout = html.Div(children=[
	dcc.Graph(figure=ceda.gender_dis('India'), config={'displayModeBar':False}),
])

