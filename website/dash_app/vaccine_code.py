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

app1 = DjangoDash('state_vaccine_1', suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets])

app1.layout = html.Div(children=[
	html.Div(children=[
		dcc.Dropdown(id='dropdown-7', options=ceda.vaccine_state_list, value='India'),
	]),
	html.Div(children=[

		dcc.Graph(id='state_vaccine_1', config={'displayModeBar':False}),
	])
])
@app1.callback(
	Output('state_vaccine_1', "figure"),
	[Input('dropdown-7', 'value')]
)
def figure1(state):
	return ceda.vaccine_administered(state)

#########################################################################

app2 = DjangoDash('state_vaccine_2', suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets])

app2.layout = html.Div(children=[
	html.Div(children=[
		dcc.Dropdown(id='dropdown-8', options=ceda.vaccine_state_list, value='India'),
	]),
	html.Div(children=[

		dcc.Graph(id='state_vaccine_2', config={'displayModeBar':False}),
	])
])
@app2.callback(
	Output('state_vaccine_2', 'figure'),
	[Input('dropdown-8', 'value')]
)
def figure2(state):
	return ceda.vaccine_total_doses(state)

##############################################################################

app3 = DjangoDash('state_vaccine_3', suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets])

app3.layout = html.Div(style={'height':'600px'}, children=[
	html.Div(children=[
		dcc.Dropdown(id='dropdown-9', style={'width':'200px'}, options=ceda.vaccine_state_list, value='India'),
	]),
	html.Div(style={'background-color':'rgba(17, 17, 17, 1)'}, className='card', children=[

		dcc.Graph(id='state_vaccine_3', config={'displayModeBar':False}),
	])
])
@app3.callback(
	Output('state_vaccine_3', 'figure'),
	[Input('dropdown-9', 'value')]
)
def figure3(state):
	return ceda.aefi(state)


####################################################
app4 = DjangoDash('state_pie_india', suppress_callback_exceptions=True, external_stylesheets=[external_stylesheets])

app4.layout = html.Div(children=[
	html.Div(children=[
		dcc.Dropdown(id='dropdown-10', style={'width':'200px'}, options=ceda.vaccine_state_list, value='India'),
	]),
	html.Div(style={'background-color':'rgba(17, 17, 17, 1)'}, className='card', children=[

		dcc.Graph(id='state_vaccine_4', config={'displayModeBar':False}),
	])
])
@app4.callback(
	Output('state_vaccine_4', 'figure'),
	[Input('dropdown-10', 'value')]
)
def figure4(state):
	return ceda.gender_dis(state)

app5 = DjangoDash('district_wise_vaccine_plot', suppress_callback_exceptions=True)

app5.layout = html.Div( children=[
	html.Br(),
		html.Div(className='row flex', children=[
			html.Div(className='col-md-6', children=[
				dcc.Dropdown(id='dropdown-7', options=ceda.vaccine_state_list_for_district, value="Maharashtra"),
		], style=dict(width='50%')),

		html.Div(className='col-md-6', children=[
			dcc.Dropdown(id='dropdown-8', options=[], value='Mumbai'),
		], style=dict(width='50%')),
	], style=dict(display='flex')),

	html.Div(className='card', children=[
		dcc.Graph(id='district_cases', config={'displayModeBar':False}),	
	])
])
@app5.callback(
	Output('dropdown-8', 'options'),
	 [Input('dropdown-7', 'value')]
)
def figure5(state):
	return ceda.make_district_list(state)

@app5.callback(
	Output('district_cases', 'figure'),
	[Input('dropdown-7', 'value'),
	 Input('dropdown-8', 'value')]
)
def figure6(state, district):
	return ceda.vaccine_district_trend(state, district)


app6 = DjangoDash('sessions_conducted_plot', suppress_callback_exceptions=True)

app6.layout = html.Div( children=[
	html.Br(),
		html.Div(className='row flex', children=[
			html.Div(className='col-md-6', children=[
				dcc.Dropdown(id='dropdown-7', options=ceda.vaccine_state_list_for_district, value="Maharashtra"),
		], style=dict(width='50%')),

		html.Div(className='col-md-6', children=[
			dcc.Dropdown(id='dropdown-8', options=[], value='Mumbai'),
		], style=dict(width='50%')),
	], style=dict(display='flex')),

	html.Div(className='card', children=[
		dcc.Graph(id='sessions_conducted_graph', config={'displayModeBar':False}),	
	])
])
@app6.callback(
	Output('dropdown-8', 'options'),
	 [Input('dropdown-7', 'value')]
)
def figure7(state):
	return ceda.make_district_list(state)

@app6.callback(
	Output('sessions_conducted_graph', 'figure'),
	[Input('dropdown-7', 'value'),
	 Input('dropdown-8', 'value')]
)
def figure8(state, district):
	return ceda.sessions_conducted(state, district)

app7 = DjangoDash('district_vaccine_type_plot', suppress_callback_exceptions=True)

app7.layout = html.Div(children=[
	html.Br(),
		html.Div(className='row flex', children=[
			html.Div(className='col-md-6', children=[
				dcc.Dropdown(id='dropdown-7', options=ceda.vaccine_state_list_for_district, value="Maharashtra"),
		], style=dict(width='50%')),

		html.Div(className='col-md-6', children=[
			dcc.Dropdown(id='dropdown-8', options=[], value='Mumbai'),
		], style=dict(width='50%')),
	], style=dict(display='flex')),

	html.Div(className='card', children=[
		dcc.Graph(id='district_vaccine_type_graph', config={'displayModeBar':False}),	
	])
])
@app7.callback(
	Output('dropdown-8', 'options'),
	 [Input('dropdown-7', 'value')]
)
def figure9(state):
	return ceda.make_district_list(state)

@app7.callback(
	Output('district_vaccine_type_graph', 'figure'),
	[Input('dropdown-7', 'value'),
	 Input('dropdown-8', 'value')]
)
def figure10(state, district):
	return ceda.district_vaccine_type(state, district)


app8 = DjangoDash('dose_administered_plot', suppress_callback_exceptions=True)

app8.layout = html.Div(children=[
	html.Br(),
		html.Div(className='row flex', children=[
			html.Div(className='col-md-6', children=[
				dcc.Dropdown(id='dropdown-7', options=ceda.vaccine_state_list_for_district, value="Maharashtra"),
		], style=dict(width='50%')),

		html.Div(className='col-md-6', children=[
			dcc.Dropdown(id='dropdown-8', options=[], value='Mumbai'),
		], style=dict(width='50%')),
	], style=dict(display='flex')),

	html.Div(className='card', children=[
		dcc.Graph(id='dose_administered_graph', config={'displayModeBar':False}),	
	])
])
@app8.callback(
	Output('dropdown-8', 'options'),
	 [Input('dropdown-7', 'value')]
)
def figure11(state):
	return ceda.make_district_list(state)

@app8.callback(
	Output('dose_administered_graph', 'figure'),
	[Input('dropdown-7', 'value'),
	 Input('dropdown-8', 'value')]
)
def figure12(state, district):
	return ceda.dose_administered(state, district)


