from django.contrib import admin
from . models import Continents, Demographic, Economic

# Register your models here.
admin.site.register(Continents)
admin.site.register(Demographic)
admin.site.register(Economic)