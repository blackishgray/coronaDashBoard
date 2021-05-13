#!/usr/bin/env python
# coding: utf-8

import numpy as np 
import pandas as pd 
import requests
import warnings
import json
import matplotlib.pyplot as plt 
import plotly.express as px
import plotly.graph_objects as go

# from datetime import datetime, timedelta

mapbox_access_token =  'pk.eyJ1IjoiYmxhY2tpc2hncmF5IiwiYSI6ImNrbzQ2eDlzNTBtcW8ydXBkbGo2ODBxejUifQ.j-pYET58qvPgO9og--uQ-g'
px.set_mapbox_access_token(mapbox_access_token)

warnings.simplefilter(action="ignore")


#Connecting to the API used from rapidapi.com
url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-key': "5930ac7ab0mshff4b750b36ae8c9p155fa3jsn352de650a898",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

#response sorted on the basis of States in INDIA
text = response.json()['state_wise']


#Converting the data of a particular district into a df 
def district_delta(state,district):
    text3 = response.json()['state_wise'][state]['district'][district]['delta']
    return pd.DataFrame(text3, index=[0])


#Function used to convert the dtypes of a col in a particular df
def make_int(df, cols):
    for i in cols:
        df[i] = df[i].astype(int)


#Json sorting on the basis of a particular district
def new_json(state):
    text2 = response.json()['state_wise'][state]['district']
    return text2


#Making a state wise df from the collected json respose earlier
def state_data():
    df = pd.DataFrame.from_dict(text)
    df = df.transpose().reset_index()
    df.drop(['statenotes', 'district', 'statecode', 'state'], axis=1, inplace=True)
    df.columns = ['state', 'active', 'confirmed', 'deaths', 'deltaconfirmed',
           'deltadeaths', 'deltarecovered', 'lastupdatedtime', 'migratedother',
           'recovered']
    make_int(df, ['active', 'confirmed', 'deaths', 'deltaconfirmed', 'deltadeaths', 'deltarecovered', 'migratedother', 'recovered'])
    df['recovery rate'] = df['recovered'] / df['confirmed']
    df['death rate'] = df['deaths'] / df['confirmed']
    return df


data_state_wise = state_data()
# data_state_wise.head()


#Setting the date for vizulatizing and display purposes
date = data_state_wise['lastupdatedtime'][0]
# date


#Intialzing the df
data_state_wise = state_data()
# data_state_wise.head()


#Making a overall i.e total counts of all the types of Cases reporte in a particular State 
def overall_df(state):
    df2 = pd.DataFrame.from_dict(new_json(state)).reset_index()
    df_3 = df2.transpose().reset_index()
    df_3.drop(0, inplace=True)
    df_3.columns = ['District', 'Notes', 'Active', 'Confirmed', 'Migrated Other', 'Deceased', 'Recovered', 'Delta']
    df_3.drop('Notes', axis=1, inplace=True)
    make_int(df_3, ['Active', 'Confirmed', 'Migrated Other', 'Deceased', 'Recovered'])
    df_3.drop(df_3[df_3['Recovered']==0].index, inplace=True, axis=0)
    df_3['recovery rate'] = df_3['Recovered']/df_3['Confirmed']
    df_3['death rate'] = df_3['Deceased']/df_3['Confirmed']
    df_3.reset_index()
    return df_3


# Init the df
overall_district_wise = overall_df('Maharashtra')
# overall_district_wise.head()

#Making a df of a particular state based on the data collected on the previous day i.e 
#Current Count of cases reported and recorded in the State 
def current_df(state):
    state = state.title()
    df_3 = overall_df(state)
    text2 = response.json()['state_wise'][state]['district']
    new_df1 = pd.DataFrame()
    for i in df_3['District']:
        new_df1 = pd.concat([new_df1, district_delta(state, i)])
    new_df1['district'] = df_3['District'].tolist()
    new_df1 = new_df1.set_index('district')
    new_df1 = new_df1.reset_index()
    return new_df1

current_district_wise = current_df('Maharashtra')
# current_district_wise.head()


# Line plot of recovery and death rate in specific states of India
def recvry_death_rate_india():
    fig = px.line(data_state_wise, x='state', y=['recovery rate', 'death rate'])
    fig.update_layout(template='plotly_dark', title=f'Recovery and Death rate in India.', hovermode='x', hoverlabel=dict(
        bgcolor='white',
        font_size=18,
        font_family='Helvetica'
    ), showlegend=False)
    fig.update_traces(hovertemplate='%{y}')
    fig.update_yaxes(title='Scale in %', showgrid=False)
    fig.update_xaxes(title='State', showgrid=False)
    return fig

# recvry_death_rate_india()


#Recovery and death rate in various districts of a particular state
def recvry_rate_state(state):
    overall_district_wise = overall_df(state)
    fig = px.line(data_frame=overall_district_wise, x='District', y=['recovery rate', 'death rate'])
    fig.update_layout(title='Recovery and Death Rate in Districts of Maharahstra.', template='plotly_dark', hovermode='x', hoverlabel=dict(
        bgcolor='white',
        font_size=18,
        font_family='Helvetica'
    ), showlegend=False)
    fig.update_traces(hovertemplate='%{y*100}')
    fig.update_yaxes(title='Rate in decimal', showgrid=False, side='right')
    fig.update_xaxes(showgrid=False)
    return fig


# recvry_rate_state('Maharashtra')

# current_district_wise.head()


#Bar graph vizualization based on the cases recorded yesterday
def bar_graph_for_current(state,status):
    current_district_wise = current_df(state)
    status = status.lower()
    if status == 'active':
        clr = 'blue'
    elif status=='confirmed':
        clr = 'darkorchid'
    elif status=='recovered':
        clr = 'green'
    else:
        clr = 'red'
    fig = px.bar(current_district_wise, x=current_district_wise['district'], y=status.lower(), color_discrete_sequence=[clr], opacity=0.7)
    fig.update_layout(title=f"Current status of {status.capitalize()} Cases of COVID-19 reported on {date}", template='plotly_dark', hoverlabel=dict(
        font_size=20,
        font_family='Helvetica',
    ))
    fig.update_traces(hovertemplate='%{y}')
    fig.update_yaxes(title=f'{status.capitalize()}', showgrid=False)
    fig.update_xaxes(title=f'{state.capitalize()}', showgrid=False)
    return fig


# bar_graph_for_current('Maharashtra', 'confirmed')

#Bar graph for overall cases reported in a particular state's 
#districts till date
def bar_graph_overall(state, status):
    overall_district_wise = overall_df(state)
    status = status.lower()
    if status == 'active':
        clr = 'blue'
    elif status=='confirmed':
        clr = 'darkorchid'
    elif status=='recovered':
        clr = 'green'
    else:
        clr = 'red'
    fig = px.bar(overall_district_wise, x=overall_district_wise['District'], y=status.capitalize(), color_discrete_sequence=[clr])
    fig.update_layout(title= f"Overall status of {status.capitalize()} Cases of COVID-19 in {state.title()} as of {date}", template='plotly_dark', 
                     hoverlabel=dict(
                         font_size=20,
                         font_family='Helvetica'
                     ))
    fig.update_traces(hovertemplate='%{y}')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    return fig


# bar_graph_overall('Maharashtra', 'Confirmed')

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='app')

list1 = data_state_wise['state']

lat_lon1 = []
for i in list1:
    i = geolocator.geocode(i)
    if i is None:
        lat_lon1.append(np.nan)
    else:
        geo = (i.latitude, i.longitude)
        lat_lon1.append(geo)


data_state_wise['locations'] = lat_lon1

data_state_wise.dropna(inplace=True)

lat, lon = zip(*np.array(data_state_wise['locations']))

data_state_wise['lat'] = lat
data_state_wise['lon'] = lon


# data_state_wise.head()

def df_for_display():
    display_df = pd.DataFrame()
    display_df['Confirmed'] = data_state_wise['confirmed']
    display_df['Active'] = data_state_wise['active']
    display_df['Deaths'] = data_state_wise['deaths']
    return display_df

#plot for total cases reported on a particular status
#throught India in a choropleth Map
def india_cases(status):
    status = status.lower()
    if status == 'active':
        clr = 'blue'
    elif status=='confirmed':
        clr = 'darkorchid'
    elif status=='recovered':
        clr = 'green'
    else:
        clr = 'red'
    fig = px.scatter_mapbox(
        data_frame=data_state_wise,
        hover_name='state',
        hover_data=[f'{status.lower()}'],
        color_discrete_sequence=[clr],
        mapbox_style="carto-darkmatter",
        size=status.lower(),
        size_max=90,
        lat='lat',
        lon = 'lon',
        zoom=3,
        opacity=0.5,
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, title = f"Status of overall   COVID-19 Cases in India.", template='plotly_dark', hoverlabel=dict(
        bgcolor=clr,
        font_size=16,
        font_family='Helvetica',
    ))
    # fig.update_traces(hovertemplate='%{hover_data}')
    return fig


# india_cases('deaths')




