from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('continents/', views.ContinentsView, name="demo"),
    path('demographics/', views.DemographicsView, name="demo"),
    path('economics/', views.DemographicsView, name="demo"),
]