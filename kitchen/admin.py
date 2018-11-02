from django.contrib import admin
from kitchen.models import Ingredient, Product


admin.site.register(Ingredient)
admin.site.register(Product)