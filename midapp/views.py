from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') 

def stopwatch(request):
    return render(request, 'stopwatch.html')


def chat(request):
    return render(request, 'chat.html')

def hello(request):
    return render(request, "profile.html")

    
