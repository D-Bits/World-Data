from django.urls import path
from . import views
from . views import (
    Index,
    ContinentsView,
    DemographicsView,
    EconomicsView,
    NationDetailView
)

urlpatterns = [
    path('', views.Index, name="index"),
    path('continents/', ContinentsView.as_view(), name="continents"),
    path('demographics/', DemographicsView.as_view(), name="demo"),
    path('economics/', EconomicsView.as_view(), name="econ"),
    path('<int:pk>/', NationDetailView.as_view(), name="natdetail")
]