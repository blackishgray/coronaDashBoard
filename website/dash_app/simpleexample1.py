import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash


#import for dash file
from website.dash_app import coronaAPI1 as capi
from website.dash_app import CoronaEDA2 as ceda


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app2 = DjangoDash('daily_cases')

app2.layout = html.Div(style={'text-align':'center'}, children=[
    html.Hr(),
    html.H3('Count of Cases Reported on each day.'),
    dcc.Dropdown(style={'width':'400px'}, id='dropdown-2',

            options=[
                {'label': 'Confirmed Cases', 'value':'dailyconfirmed'},
                {'label': "Recovered Cases", 'value':'dailyrecovered'},
                {'label': "Deceased Cases", 'value':'dailydeceased'},
            ],
            value='dailyconfirmed',
        ),
    html.Br(),
    dcc.Graph('daily_cases_plot'),
])

@app2.callback(
    Output('daily_cases_plot', 'figure'),
    [Input('dropdown-2', 'value')]
    )
def figure2(status):
    print('Done')
    return ceda.daily_count_cases_india(status)
