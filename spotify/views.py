from django.shortcuts import render

def home(request):
    templates = 'spotify/home.html'

    return render(request,templates)
