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

mapbox_access_token =  'pk.eyJ1IjoiYmxhY2tpc2hncmF5IiwiYSI6ImNrbzQ2eDlzNTBtcW8ydXBkbGo2ODBxejUifQ.j-pYET58qvPgO9og--uQ-g'
px.set_mapbox_access_token(mapbox_access_token)

warnings.simplefilter(action="ignore")


# data_state_wise.head()
url_time_series = "https://api.covid19india.org/csv/latest/case_time_series.csv"
url_vaccine_state = "http://api.covid19india.org/csv/latest/cowin_vaccine_data_statewise.csv"
url_vaccine_indian_district = 'http://api.covid19india.org/csv/latest/cowin_vaccine_data_districtwise.csv'
url_state_wise_daily = "https://api.covid19india.org/csv/latest/state_wise_daily.csv"
url_for_district_cases = 'https://api.covid19india.org/csv/latest/districts.csv'


def chg_datetime(df, cols):
    for i in cols:
        df[i] = pd.to_datetime(df[i])

def chg_numeric(df, cols):
    for i in cols:
        df[i] = pd.to_numeric(df[i])

time_series = pd.read_csv(url_time_series)
time_series.rename(columns={'Daily Confirmed':'dailyconfirmed', 'Daily Deceased':'dailydeceased', 'Daily Recovered':'dailyrecovered'}, inplace=True)
# time_series.tail()

time_series['mortality rate'] = time_series['dailydeceased'] / time_series['dailyconfirmed']
time_series['recovery rate'] = time_series['dailyrecovered'] / time_series['dailyconfirmed']

# time_series.shape

# time_series.dtypes

chg_datetime(time_series, ['Date', 'Date_YMD'])

# COVID Cases EDA


# Plot for daily cases recorded in India
def daily_count_cases_india(status):

    if status=='dailydeceased':
        clr = ['red']
    else:
        clr = ['darkturquoise']
    fig = px.area(time_series, x='Date', y=status, template='plotly_dark', color_discrete_sequence=clr)
    fig.update_layout(title="Daily Cases Reported in India", hovermode='x', hoverlabel=dict(
#         bgcolor = 'white',
        font_size=18,
        font_family='Helvetica'
    ), showlegend=True)
    fig.update_xaxes(rangeslider_visible=True, showgrid=False)
    fig.update_yaxes(showgrid=False, title=f'{str.capitalize(status[5:])} Count', side='right', showline=True, linewidth=2, linecolor='white')
    fig.update_traces(hovertemplate=f"{str.capitalize(status[5:])}: "+"%{y}")
    return fig

####################

# daily_count_cases_india('dailyconfirmed')

# time_series.tail()

#plot for recovery and death rate in India over the period of 1.5 years roughly
def recovery_death_rate_india():
    fig = px.line(time_series, x='Date', y=['recovery rate', 'mortality rate'])
    fig.update_layout(title="Recovery and Mortality Rate in India through the Pandemic", template='plotly_dark', hovermode='x', hoverlabel=dict(
        font_size=18,
        font_family='helvetica',
    ), showlegend=False)
    fig.update_xaxes(title='Date', title_font_family='Arial', showgrid=False)
    fig.update_yaxes(title='Scale(%)', title_font_family='Arial', showgrid=False, side='right', showline=True, linewidth=2, linecolor='white')
    fig.update_traces(hovertemplate='%{y}')
    # fig.update_traces(mode='markers+lines')
    return fig

# recovery_death_rate_india()

#Overall Total cases reported in India till the today
def total_cases_india():
    fig = px.area(time_series, x='Date', y=['Total Deceased','Total Recovered', 'Total Confirmed'], color_discrete_sequence=['red', 'aqua', 'coral'])
    fig.update_layout(title="Total COVID-19 Cases reported in India" ,template='plotly_dark', hovermode='x unified',hoverlabel=dict(
        font_family='helvetica',
        font_size=13,
    ), showlegend=False)
    fig.update_traces(hovertemplate='%{y}')
    fig.update_yaxes(title='Cases', side='right', showline=True, linewidth=2, linecolor='white')
    fig.update_xaxes(showgrid=False)
    return fig



# total_cases_india()


state_wise = pd.read_csv(url_state_wise_daily)
pd.set_option('display.max_columns', 42)
# state_wise.tail()

# state_wise.dtypes[:3]



chg_datetime(state_wise, ["Date", 'Date_YMD'])

indian_states = {
    "AN":"Andaman and Nicobar Islands", "AP":"Andhra Pradesh", "AR":"Arunachal Pradesh", "AS":"Assam", "BR":"Bihar", "CG":"Chandigarh", "CH":"Chhattisgarh",
    "DN":"Dadra and Nagar Haveli", "DD":"Daman and Diu",    "DL":"Delhi", "GA":"Goa", "GJ":"Gujarat",    "HR":"Haryana",    "HP":"Himachal Pradesh",
    "JK":"Jammu and Kashmir", "JH":"Jharkhand",  "KL":"Kerala", "KA":"Karnataka",  "LA":"Ladakh", "LD":"Lakshadweep", "MP":"Madhya Pradesh", "MH":"Maharashtra", "MN":"Manipur",
    "ML":"Meghalaya", "MZ":"Mizoram", "NL":"Nagaland", "OR":"Odisha", "PY":"Puducherry", "PB":"Punjab", "RJ":"Rajasthan", "SK":"Sikkim",
    "TN":"Tamil Nadu",  "TG":"Telangana",  "TR":"Tripura",  "UP":"Uttar Pradesh",  "UT":"Uttarakhand",  "WB":"West Bengal"
}



state_wise = state_wise.rename({'TT': 'Total Cases'}, axis=1)
state_wise = state_wise.rename(indian_states, axis=1)



state_wise['Maharashtra']  = abs(state_wise['Maharashtra'])

state_wise[state_wise['Date']=='15/12/2020']

state_names = state_wise.columns[4:]

state_names_as_options=[{'label':a , 'value':a} for a in state_names]

# state_df = [state_wise_confirmed, state_wise_deceased, state_wise_recovered]

# Plot for vizualization of Cases reported in a 
# particular state
def plot_trend_line(state, status):
    if status.capitalize()=='Deceased':
        clr = ['red']
    else:
        clr=['pink']
    df = state_wise[state_wise['Status']==status.capitalize()].reset_index()
    fig = px.area(df, x='Date', y=state, color='Status', color_discrete_sequence=clr)
    fig.update_layout(template='plotly_dark', hovermode='x unified',hoverlabel=dict(
        font_size=20,
        font_family='Helvetica',
    ))
    fig.update_xaxes(rangeslider_visible=True, showgrid=False)
    fig.update_yaxes(title=f"{df['Status'][0]} Cases of COVID-19 in {state.title()}", showgrid=False, showline=True, linewidth=2, linecolor='white')
    fig.update_traces(hovertemplate="%{y}", mode='markers',showlegend=False)
    return fig



# plot_trend_line('Maharashtra', 'Recovered')

district_cases = pd.read_csv(url_for_district_cases)
# district_cases.head()



# district_cases.shape



# district_cases.dtypes



district_cases['Date'] = pd.to_datetime(district_cases['Date'], dayfirst=True, yearfirst=False)



#Overall Cases recorede in a particular district
def district_wise_cases(state, district):
    df = district_cases[(district_cases['State']==state) & (district_cases['District']==district)]
    fig = px.area(df, x='Date', y=['Deceased', 'Recovered', 'Confirmed'])
    fig.update_layout(title=f'Overall Case in the district {district.capitalize()} of {state.capitalize()}', template='plotly_dark', hovermode='x unified', hoverlabel=dict(
        font_size=20,
        font_family='Helvetica',
    ), )
    fig.update_traces(hovertemplate="%{y}", showlegend=False)
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, side='right', showline=True, linewidth=2, linecolor='white')
    return fig



# district_wise_cases('Maharashtra', 'Mumbai')


# #Vaccination EDA



# Vaccination EDA for States


vaccine_state_wise = pd.read_csv(url_vaccine_state)
# vaccine_state_wise.tail()



vaccine_state_wise['Updated On'] = pd.to_datetime(vaccine_state_wise['Updated On'], dayfirst=True, yearfirst=False)


vaccine_state_list=[{'label':a, 'value':a} for a in vaccine_state_wise['State'].unique()]

# vaccine_state_wise.columns

# Vaccine Administered in a particular state in India
def vaccine_administered(state):
    df = vaccine_state_wise[vaccine_state_wise['State']==state]
    fig = px.area(data_frame=df, x='Updated On', y=['Total Doses Administered', 'Second Dose Administered', 'First Dose Administered', 
                                                    'Total Covaxin Administered', 'Total CoviShield Administered'])
    fig.update_layout(title=f'Total Count of Vaccinces Administered in {state} till date.', template='plotly_dark', hovermode='x unified', hoverlabel=dict(
        font_family='Helvetica',
        font_size=12,
    ), showlegend=False )
    fig.update_traces(hovertemplate="""%{y}""")
    fig.update_xaxes(title='Date',showgrid=False)
    fig.update_yaxes(title='Amount of Viles', showgrid=False, side='right', showline=True, linewidth=2, linecolor='white')
    
    return fig

# vaccine_administered('Maharashtra')



# Vizulation of number of individuals vaccinated on the basis of gender
def vaccine_total_doses(state):
    df = vaccine_state_wise[vaccine_state_wise['State']==state]
    fig = px.area(data_frame=df, x='Updated On', y=['Transgender(Individuals Vaccinated)','Female(Individuals Vaccinated)',  'Male(Individuals Vaccinated)', 'Total Doses Administered',])
    fig.update_layout(title=f'Gender Distribution of Vaccinated Individuals in {state}', template='plotly_dark', hovermode='x unified', hoverlabel=dict(
        font_family='Helvetica',
        font_size=12,
    ), showlegend=False )
    fig.update_traces(hovertemplate="""%{y}""")
    fig.update_xaxes(title='Date', showgrid=False)
    fig.update_yaxes(title='Amount of Viles', showgrid=False, side='right', showline=True, linewidth=2, linecolor='white')
    
    return fig



# vaccine_total_doses('Maharashtra')



#Aefi plot in a particular state
def aefi(state):
    df = vaccine_state_wise[vaccine_state_wise['State']==state]
    fig = px.area(data_frame=df, x='Updated On', y=['AEFI'], color_discrete_sequence=['white'])
    fig.update_layout(title=f'AEFI of {state}', template='plotly_dark', hovermode='x unified', hoverlabel=dict(
        font_family='Helvetica',
        font_size=12,
    ), showlegend=False )
    fig.update_traces(hovertemplate="""%{y}""")
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, side='right', showline=True, linewidth=2, linecolor='white')
    return fig
# aefi('Maharashtra')

# Pie chart of each gender count in a particular state 
def gender_dis(state):
    df = vaccine_state_wise[vaccine_state_wise['State']==state]
    values = [np.sum(df['Male(Individuals Vaccinated)']), np.sum(df['Female(Individuals Vaccinated)']), np.sum(df['Transgender(Individuals Vaccinated)'])]
    labels = ['Male', 'Female', 'Transgender']

    fig = px.pie(values=values, names=labels, hole=0.4, color_discrete_sequence=['dimgrey', 'white'])
    fig.update_layout(title="Distribution of Vaccinated Population on the basis of Gender ",template='plotly_dark', showlegend=False)
    fig.update_traces(hovertemplate='%{label}: %{value}', hoverlabel=dict(
        font_size=20,
        font_family="Arial",
#         bgcolor='white'
    ))
    return fig



# gender_dis('Maharashtra')

# Vaccination EDA for District wise data

district_vaccine = pd.read_csv(url_vaccine_indian_district)

# district_vaccine.shape

# district_vaccine.columns

district_vaccine.drop(['S No', 'State_Code',  'District_Key', 'Cowin Key'], inplace=True, axis=1)

# district_vaccine.head()

vaccine_state_list_for_district = [{'label':a, 'value':a} for a in district_vaccine['State'].unique()][1:]

def make_district_list(state):
    list_2 = district_vaccine[district_vaccine['State']==state]['District'].unique()
    return [{'label':a, 'value':a} for a in list_2]

# transforming the dataframe into a much more readable form 
# also for vizualuzation dataframe needs to be in a ceartain orientation
# hence this function takes a state and district and then transform the 
# main df into a much more process friendly orientation
def new_df(state, district):
    df = district_vaccine[(district_vaccine['State']==state)&(district_vaccine['District']==district)]
    list_of_dates = df.columns[2:].tolist()
    for i in range(len(list_of_dates)):
        list_of_dates[i] = list_of_dates[i].split('.')[0]
    list_series = pd.Series(list_of_dates)
    lu = list_series.unique().tolist()
    df1 = pd.DataFrame(columns=['State', 'District', 'Date', 'Total Individuals Registered', 'Total Sessions Conducted','Total Sites','First Dose Administered',
                                'Second Dose Administered','Male(Individuals Vaccinated)','Female(Individuals Vaccinated)',
                                'Transgender(Individuals Vaccinated)','Total Covaxin Administered','Total CoviShield Administered'])
    for a in range(2):
        df1['State'] = state
        df1['District'] = district
        df1['Date'] = lu
        df1['Total Individuals Registered'] = [df[lu[i]].tolist()[0] for i in range(len(lu))]
        df1['Total Sessions Conducted'] = [df[lu[i] + '.1'].tolist()[0] for i in range(len(lu))]
        df1['Total Sites'] = [df[lu[i] + '.2'].tolist()[0] for i in range(len(lu))]
        df1['First Dose Administered'] = [df[lu[i] + '.3'].tolist()[0] for i in range(len(lu))]
        df1['Second Dose Administered'] = [df[lu[i] + '.4'].tolist()[0] for i in range(len(lu))]
        df1['Male(Individuals Vaccinated)'] = [df[lu[i] + '.5'].tolist()[0] for i in range(len(lu))]
        df1['Female(Individuals Vaccinated)'] = [df[lu[i] + '.6'].tolist()[0] for i in range(len(lu))]
        df1['Transgender(Individuals Vaccinated)'] = [df[lu[i] + '.7'].tolist()[0] for i in range(len(lu))]
        df1['Total Covaxin Administered'] = [df[lu[i] + '.8'].tolist()[0] for i in range(len(lu))]
        df1['Total CoviShield Administered'] = [df[lu[i] + '.9'].tolist()[0] for i in range(len(lu))]
        df1['Date'] = pd.to_datetime(df1['Date'], dayfirst=True, yearfirst=False)
        chg_numeric(df1, ['Total Individuals Registered', 'Total Sessions Conducted','Total Sites','First Dose Administered',
                          'Second Dose Administered','Male(Individuals Vaccinated)','Female(Individuals Vaccinated)',
                          'Transgender(Individuals Vaccinated)','Total Covaxin Administered','Total CoviShield Administered'])
        df1.reset_index()
    return df1


# mumbai_df = new_df('Maharashtra', 'Mumbai')
# mumbai_df.tail()



# mumbai_df.dtypes

#Distribution of vaccinated people on basis of gender in a particular district of that state
def vaccine_district_trend(state, district):
    df = new_df(state, district)
    fig = px.line(df, x='Date', y=['Transgender(Individuals Vaccinated)', 'Female(Individuals Vaccinated)', 'Male(Individuals Vaccinated)', 'Total Individuals Registered'])
    fig.update_layout(title='Vaccination of Individual Gender.', template='plotly_dark', hoverlabel=dict(
        font_size=12,
        font_family='Helvetica',
    ), hovermode='x', showlegend=False)
    fig.update_traces(hovertemplate='%{y}')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, side='right', showline=True, linewidth=2, linecolor='white')
    return fig

# vaccine_district_trend('Maharashtra', 'Mumbai')

# mumbai_df.tail()



#session of vaccination conducted in a particular district
def sessions_conducted(state, district):
    df = new_df(state, district)
    fig = px.bar(df, x='Date', y='Total Sessions Conducted', color_discrete_sequence=['indianred'], opacity=0.9)
    fig.update_layout(title=f'Vaccination Sessions Conducted in {district} of state {state}', template='plotly_dark', hovermode='x', hoverlabel=dict(
#         bgcolor='white',
        font_size=12,
        font_family='Helvetica'
    ))
    fig.update_traces(hovertemplate='%{y}')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, side='right', showline=True, linewidth=2, linecolor='white')
    return fig



# sessions_conducted('Maharashtra', 'Mumbai')



# type of vaccine administered on each day in a particular district
def district_vaccine_type(state, district):
    df = new_df(state, district)
    fig = px.area(df, x='Date', y=['Total Covaxin Administered', 'Total CoviShield Administered'], color_discrete_sequence=['coral', 'mistyrose'])
    fig.update_layout(title=f'Vaccination Sessions Conducted in {district} of state {state}', template='plotly_dark', hovermode='x', hoverlabel=dict(
#         bgcolor='white',
        font_size=12,
        font_family='Helvetica'
    ), showlegend=False)
    fig.update_traces(hovertemplate='%{y}')
    fig.update_yaxes(side='right', showgrid=False, showline=True, linewidth=2, linecolor='white')
    return fig



# district_vaccine_type('Maharashtra', 'Mumbai')



# Dose number administered to individuals
def dose_administered(state, district):
    df = new_df(state, district)
    fig = px.area(df, x='Date', y=['Second Dose Administered', 'First Dose Administered'], color_discrete_sequence=['pink', 'aqua'])
    fig.update_layout(title=f'Vaccination Sessions Conducted in {district} of state {state}', template='plotly_dark', hovermode='x', hoverlabel=dict(
#         bgcolor='white',
        font_size=20,
        font_family='Helvetica'
    ), showlegend=False)
    fig.update_traces(hovertemplate='%{y}')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, side='right', showline=True, linewidth=2, linecolor='white')
    return fig



# dose_administered('Maharashtra', 'Mumbai')

def cities_of_state(state):
    cities = district_cases[district_cases['State']==state]['District'].unique()
    return [{'label':a , 'value':a} for a in cities]





