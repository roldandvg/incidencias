from django.shortcuts import render, render_to_response

# Create your views here.
def inicio(self):
	return render_to_response('base.html')
