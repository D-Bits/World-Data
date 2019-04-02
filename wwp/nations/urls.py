from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('continents/', views.ContinentsView, name="continents"),
    path('demographics/', views.DemographicsView, name="demo"),
    path('economics/', views.DemographicsView, name="econ"),
    path('<int:pk>/', views.NationDetailView, name="natdetail")
]