from django import forms
from kitchen.models import Product, Ingredient, ProductIngredient


class ProductIngredientForm(forms.Form):
    name = forms.CharField(label='Snack Name', max_length=100, required=False)
    # ingredients = forms.ModelChoiceField(Ingredient.objects.all())
    ingredients = Ingredient.objects.all()

