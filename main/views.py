from django.shortcuts import render, redirect
from django.shortcuts import loader
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse

#def index(request):
#	template = loader.get_template('home.html')
#	return HttpResponse(template.render())

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def homepage(request):
	template = loader.get_template('main/register.html')
	return HttpResponse(template.render())
