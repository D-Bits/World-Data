from django.db import models

# Create models for continents
class Continents(models.Model):

    name = models.CharField(max_length=150)
    total_population = models.CharField(max_length=150)
    countries = models.IntegerField() #  Number of countries in continent

# Model for demographic data
class Demographic(models.Model):

    name = models.CharField(max_length=150)
    region = models.CharField(max_length=150)
    gov_type = models.CharField(max_length=150) #  Government type
    total_population = models.IntegerField()

# Model for economic data    
class Economic(models.Model):

    name = models.CharField(max_length=150)
    gdp = models.DecimalField(max_digits=6, decimal_places=2)
    gdp_per_capita = models.DecimalField(max_digits=5, decimal_places=2)
    gini = models.DecimalField(max_digits=4, decimal_places=2)
    unemployment = models.DecimalField(max_digits=4, decimal_places=2)
    poverty_rate = models.DecimalField(max_digits=4, decimal_places=2)
