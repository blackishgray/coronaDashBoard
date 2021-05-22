from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from website.dash_app import dash_code, states_code

# Create your views here.
def index(request):
	return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def resources(request):
	return render(request, 'resources.html')