from django import forms
from kitchen.models import Product, Ingredient, ProductIngredient


class ProductForm(forms.Form):
    name = forms.CharField(label='Snack Name', max_length=100, required=False)
    # ingredients = forms.ModelChoiceField(Ingredient.objects.all())
    # ingredients = Ingredient.objects.all()

    def save(self, commit=True):
        p = Product()
        p.name = self.cleaned_data['name']
        p.save()
        return p


class ProductIngredientForm(forms.ModelForm):
    class Meta:
        model = ProductIngredient
        fields = ['amount', 'ingredient']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'price']
