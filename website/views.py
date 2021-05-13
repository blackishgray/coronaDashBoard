from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go

from website.dash_app import dash_code, states_code

# Create your views here.
def index(request):
	# a = spare_file.sum(3, 4)
	context = {
	"name": 'Ratna',
	# 'a': a
	}
	return render(request, 'index.html', context=context)

def india(request):
    return render(request, 'india.html')

def states(request):
    return render(request, 'states.html')

