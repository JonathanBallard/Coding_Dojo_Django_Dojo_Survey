from django.urls import path
from . import views

urlpatterns = [
    path('', views.randomWord),
    path('reset/', views.reset),
    
]