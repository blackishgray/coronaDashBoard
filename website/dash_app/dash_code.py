# import os 
# import dash
# import dash_table
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.graph_objs as go
# import dash_bootstrap_components as dbc

# from django_plotly_dash import DjangoDash

# #import for dash file
# from website.dash_app import coronaAPI1 as capi
# from website.dash_app import CoronaEDA2 as ceda

# from flask import send_from_directory

# external_stylesheets =  r'C:/Users/Ratnadeep Gawade/Desktop/python/django/coronaApp/app/website/assets/style.css'
# app1 = DjangoDash('india_plot', suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets])

# ###################################################################
# #######figure 1 #################
# app1.layout = html.Div(id='main-div', children=[

# 	html.Br(),

# 		dcc.Dropdown(className='dropdown',id='dropdown-1',
# 			style={'width':'200px'},
# 			options=[
# 				{'label': 'Confirmed Cases', 'value':'confirmed'},
# 				{'label': "Recovered Cases", 'value': 'recovered'},
# 				{'label': "Deceased Cases",  'value': 'deaths'},
# 				{'label':'Active Cases', 	 'value':'active'},
# 			],
# 			value='confirmed',
# 			),
# 		html.Br(),
# 		html.Div(children=[
# 			dcc.Graph(id='india_map', config={'displayModeBar':False}),
# 		]),
# ])

# @app1.callback(
# 	Output('india_map', 'figure'),
# 	[Input('dropdown-1', 'value')]
# 	)
# def figure1(status):
# 	return capi.india_cases(status)

# # #################################################################
# # #########figure 2 #########################



# app2 = DjangoDash('total_cases_india_line_graph')

# app2.layout = html.Div(children=[
# 	html.Br(),

# 	html.Div(className='card', id='div2', children=[

# 		html.Br(),
# 		dcc.Graph(figure=ceda.total_cases_india(), config={'displayModeBar':False}),
# 		]),
# ])

# # #########################################################
# # #################figure 3 ######################
# app3 = DjangoDash('daily_cases', external_stylesheets=[external_stylesheets])

# app3.layout = html.Div(children=[

# 	html.Br(),

# 	html.Div(children=[

# 		dcc.Dropdown(className='dropdown',id='dropdown-2', 
# 			style={'width':'200px'},
# 			options=[
# 				{'label': 'Confirmed Cases', 'value':'dailyconfirmed'},
# 				{'label': "Recovered Cases", 'value':'dailyrecovered'},
# 				{'label': "Deceased Cases",  'value':'dailydeceased'},
# 			],
# 			value='dailyconfirmed',
# 			placeholder='Select a status you want to vizualize..'
# 			),
# 		html.Br(),
# 		dcc.Graph(id='daily_count_cases', config={'displayModeBar':False}),
# 		]),
# ])
# @app3.callback(
# 	Output('daily_count_cases', 'figure'),
# 	[Input('dropdown-2', 'value')]
# 	)
# def figure3(status):
# 	return ceda.daily_count_cases_india(status)


# # #################################################
# # ############figure 4##############
# app4 = DjangoDash('recovry_death_india', external_stylesheets=[external_stylesheets])

# app4.layout = html.Div(children=[
# 	html.Br(),

# 	html.Div(children=[

# 		html.Br(),
# 		dcc.Graph(figure=ceda.recovery_death_rate_india(), config={'displayModeBar':False}),
# 		]),
# ])


# app3 = DjangoDash('state_vaccine_1', suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets])

# app3.layout = html.Div(children=[
# 	html.Div(children=[
# 		dcc.Dropdown(id='dropdown-7', options=ceda.vaccine_state_list, value='India'),
# 	]),
# 	html.Div(children=[

# 		dcc.Graph(id='state_vaccine_1', config={'displayModeBar':False}),
# 	])
# ])
# @app3.callback(
# 	Output('state_vaccine_1', "figure"),
# 	[Input('dropdown-7', 'value')]
# )
# def figure4(state):
# 	return ceda.vaccine_administered(state)

# #########################################################################

# app4 = DjangoDash('state_vaccine_2', suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets])

# app4.layout = html.Div(children=[
# 	html.Div(children=[
# 		dcc.Dropdown(id='dropdown-8', options=ceda.vaccine_state_list, value='India'),
# 	]),
# 	html.Div(children=[

# 		dcc.Graph(id='state_vaccine_2', config={'displayModeBar':False}),
# 	])
# ])
# @app4.callback(
# 	Output('state_vaccine_2', 'figure'),
# 	[Input('dropdown-8', 'value')]
# )
# def figure5(state):
# 	return ceda.vaccine_total_doses(state)

# ##############################################################################

# app5 = DjangoDash('state_vaccine_3', suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets])

# app5.layout = html.Div(style={'height':'600px'}, children=[
# 	html.Div(children=[
# 		dcc.Dropdown(id='dropdown-9', style={'width':'200px'}, options=ceda.vaccine_state_list, value='India'),
# 	]),
# 	html.Div(style={'background-color':'rgba(17, 17, 17, 1)'}, className='card', children=[

# 		dcc.Graph(id='state_vaccine_3', config={'displayModeBar':False}),
# 	])
# ])
# @app5.callback(
# 	Output('state_vaccine_3', 'figure'),
# 	[Input('dropdown-9', 'value')]
# )
# def figure5(state):
# 	return ceda.aefi(state)


# ####################################################
# app6 = DjangoDash('state_pie_india', suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets])

# app6.layout = html.Div(children=[
# 	html.Div(children=[
# 		dcc.Dropdown(id='dropdown-10', style={'width':'200px'}, options=ceda.vaccine_state_list, value='India'),
# 	]),
# 	html.Div(style={'background-color':'rgba(17, 17, 17, 1)'}, className='card', children=[

# 		dcc.Graph(id='state_vaccine_4', config={'displayModeBar':False}),
# 	])
# ])
# @app6.callback(
# 	Output('state_vaccine_4', 'figure'),
# 	[Input('dropdown-10', 'value')]
# )
# def figure5(state):
# 	return ceda.gender_dis(state)