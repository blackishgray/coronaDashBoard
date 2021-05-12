from django.urls import path 

from . import views
from website.dash_app import simpleexample, simpleexample1, spare_file

urlpatterns = [
	path('', views.index, name='index'),
	path('figure', views.home, name='home'),
	path('new', views.new, name='new'),
]