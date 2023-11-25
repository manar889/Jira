from django.shortcuts import render, redirect
from django.http import HttpResponse






# Create your views here.
def home(request):
    return render(request, "ICS/home.html")

def signup(request):
   
    return render(request, "ICS/signup.html")  

def index(request):
    return render(request, "ICS/index.html")  

def blogdetails(request):
    return render(request, "ICS/blog-details.html")              