from django.urls import path
from midapp import views

urlpatterns = [
    path('stop', views.stopwatch),
    path('chat', views.chat),
    path('', views.home),
<<<<<<< HEAD
    path("hemanth", views.hemanth, name="hemanth"),
]
=======
    path("hello", views.hello, name="hello")
]

>>>>>>> 5cb7264e4dac33ffa5828793e0559ba48b87603b
