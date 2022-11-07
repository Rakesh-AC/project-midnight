from django.urls import path
from midapp import views

urlpatterns = [
    path('stop', views.stopwatch),
    path('chat', views.chat),
    path('', views.home),
]