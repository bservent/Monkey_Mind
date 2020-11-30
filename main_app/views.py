from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def browse(request):
    return render(request, 'browse.html')
