from django.contrib import admin
from kitchen.models import Ingredient, Product, ProductIngredient


admin.site.register(Ingredient)
admin.site.register(Product)
admin.site.register(ProductIngredient)