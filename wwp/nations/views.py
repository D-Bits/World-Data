from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Demographic, Economic, Continents


# Home page view
def index():
    
    template_name = 'nations/index.html'
    return render(template_name)


# Continents views
class ContinentsView(ListView):

    model = Continents
    template_name = 'nations/continents.html'
    context_object_name = 'continents'
    ordering = ['-name']


# Demographics views
class DemographicsView(ListView):

    model = Demographic
    template_name = 'nations/demographics.html'
    context_object_name = 'nations'
    ordering = ['-name']
    title = 'Demographic Data'


# Economics view
class EconomicsViews(ListView):

    model = Economic
    template_name = 'nations/economics.html'
    context_object_name = 'nations'
    ordering = ['-name']
    title = 'Economic Data'

class NationDetailView(DetailView):

    model = Economic, Demographic
    template = 'nations/nation_detail.html'
    