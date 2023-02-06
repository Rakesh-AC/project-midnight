from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') 

def stopwatch(request):
    return render(request, 'stopwatch.html')


def chat(request):
    return render(request, 'chat.html')

def hemanth(request):
    return render(request, "profile.html")

def hello(request):
    print("hello world")
    return render(request, "hello.html")
    

    
