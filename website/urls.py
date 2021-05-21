from django.urls import path 

from . import views
from website.dash_app import CoronaEDA2, coronaAPI1, cases_code, vaccine_code

urlpatterns = [
	path('', views.index, name='index'),
	path('india', views.dashboard, name='dashboard'),
	path('resources', views.resources, name='resources')
]