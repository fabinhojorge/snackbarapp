from django import forms
from kitchen.models import Product, Ingredient, ProductIngredient


class SnackForm(forms.Form):
    name = forms.CharField(label='Snack Name', max_length=100, required=False)
    ingredients = forms.ModelChoiceField(Ingredient.objects.all())
    amount = forms.DecimalField(label="Amount", max_digits=2, decimal_places=0)

    # It´s expected that the ingredients and amount would be a pair.
    # But for now we will not create the validator functions

    def save(self, commit=True):
        # Missing the validation function.


        data = dict(self.data)
        p = Product()
        p.name = data['name'][0]
        p.save()

        ing_amount = zip(data['ingredients'], data['amount'])
        for i in ing_amount:
            prd_ing = ProductIngredient()
            prd_ing.ingredient = Ingredient.objects.get(id=i[0])
            prd_ing.product = p
            prd_ing.amount = i[1]
            prd_ing.save()
        # prd_ing.product = p
        # prd_ing.ingredient = Ingredient.objects.get(id=ing_id)


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'price']
