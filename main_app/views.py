from django.shortcuts import render, redirect, get_object_or_404
from .models import Meditation, User, Category



def home(request):
    return render(request, 'home.html')

def browse(request):
    return render(request, 'browse.html')

def register(request):
    return render(request, 'register.html')

def signin(request):
    return render(request, 'signin.html')
