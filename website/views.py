from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
from django.core.mail import send_mail
from django.conf import settings
from website.dash_app import dash_code, states_code

# Create your views here.
def index(request):
	# a = spare_file.sum(3, 4)
	context = {
	"name": 'Ratna',
	# 'a': a
	}
	return render(request, 'index.html', context=context)

def dashboard(request):
    return render(request, 'dashboard.html')

def states(request):
    return render(request, 'states.html')

def form(request):
	if request.method=='POST':
		email = request.POST['email']
		message = request.POST['message']
		send_mail(
	    	'test',
	    	message,
	    	settings.EMAIL_HOST_USER,
	    	[email],
	    	fail_silently=False,
			)
	return render(request, 'forms.html')