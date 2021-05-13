from django.urls import path 

from . import views
from website.dash_app import CoronaEDA2, coronaAPI1, dash_code, states_code

urlpatterns = [
	path('', views.index, name='index'),
	path('india', views.india, name='india'),
	path('states', views.states, name='states'),
]