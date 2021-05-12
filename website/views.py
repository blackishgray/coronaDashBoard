from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

from website.dash_app import spare_file
from website.dash_app import dash_code

# Create your views here.
def index(request):
	a = spare_file.sum(3, 4)
	context = {
	"name": 'Ratna',
	'a': a
	}
	return render(request, 'index.html', context=context)

def home(request):
    return render(request, 'dash_demo.html')

def new(request):
    return render(request, 'dash_demo1.html')

