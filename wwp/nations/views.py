from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from . models import Demographic, Economic, Continents


# Home page view
class Index(TemplateView):

    title = 'Home'
    template_name = 'nations/index.html'


# Continents views
class ContinentsView(ListView):

    model = Continents
    template_name = 'nations/continents.html'
    context_object_name = 'continents'
    ordering = ['name']
    title = 'Continents Data'


# Demographics data for all countries
class DemographicsView(ListView):

    model = Demographic
    template_name = 'nations/demographics.html'
    context_object_name = 'demographics'
    #queryset = Demographic.objects.all()
    ordering = ['name']
    title = 'Demographic Data'

    # Define the queryset

# Economics data for all countries
class EconomicsView(ListView):

    model = Economic
    template_name = 'nations/economics.html'
    context_object_name = 'nations'
    ordering = ['-name']
    title = 'Economic Data'


# View for info on an individual nation 
class NationDetailView(DetailView):

    model = Economic
    template = 'nations/nation_detail.html'
    
    # Select data from all fields from Demographic and Economic models
    def queryset():
        
        Economic.objects.all().select_related('name')
    

