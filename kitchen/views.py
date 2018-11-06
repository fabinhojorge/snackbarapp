from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from kitchen.models import Product, Ingredient, ProductIngredient
from kitchen.form import SnackForm, IngredientForm


def index(request):
    data = dict()
    data['snacks'] = get_list_or_404(Product)
    return render(request, 'kitchen/index.html', data)


def ingredient(request):
    data = dict()
    form_ingredient = IngredientForm(request.POST or None)

    if form_ingredient.is_valid():
        form_ingredient.save()
        form_ingredient = IngredientForm()
        data['ingredient_saved'] = True

    data['ingredient_form'] = form_ingredient
    data['ingredients'] = Ingredient.objects.all().order_by('-id')
    return render(request, 'kitchen/ingredient.html', data)


def createsnack(request):
    data = dict()

    snack_form = SnackForm(request.POST or None)
    if snack_form.is_valid():
        # p = product_form.save(request)
        snack_form.save()
        data['snack_saved'] = True
        # return redirect('url_listagem')

    data['snack_form'] = snack_form
    return render(request, 'kitchen/createsnack.html', data)
