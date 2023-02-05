from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') 

def stopwatch(request):
    return render(request, 'stopwatch.html')


def chat(request):
    return render(request, 'chat.html')

<<<<<<< HEAD
def hemanth(request):
    return render(request, "profile.html")
=======
def hello(request):
    return render(request, "profile.html")

    
>>>>>>> 5cb7264e4dac33ffa5828793e0559ba48b87603b
