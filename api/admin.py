from django.contrib import admin
from .models import Item, Location

def register(model):
    admin.site.register(model)

register(Item)
register(Location)

