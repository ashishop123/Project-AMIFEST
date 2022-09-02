from django import forms
from django.shortcuts import render
from .models import event
from .forms import usersform
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    event_list = event.objects.all
    return render(request,'home.html', 
    {'event_list': event_list})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def upcoming(request):
    return render(request,'upcoming.html')

def happening(request):
    return render(request,'happening.html')

def popular(request):
    return render(request,'popular.html')

def register(request):
    submitted = False
    if request.method == "POST":
        form = usersform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = usersform
        if 'submitted' in request.GET:
            submitted=True

    return render(request, 'register.html', {'form':form, 'submitted':submitted})

    
    
