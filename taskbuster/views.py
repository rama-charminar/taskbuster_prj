from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic import View
from django.shortcuts import render
import sqlite3

def Rama(request):		
	return render(request, 'rama.htm')
def List(request):		
	return render(request, 'blog/list.html')
def index(request):		
	return render(request, 'index.html')
def rama(request):
	message = 'You submitted an empty form.'
	
	if 'your_name' in request.POST:
		name=request.POST['your_name']
		#'current_nameentered'.value=name
	return HttpResponse(name)
			
