from django.shortcuts import render, get_object_or_404, get_list_or_404
from kitchen.models import Product, Ingredient, ProductIngredient
from kitchen.form import ProductIngredientForm, ProductForm, IngredientForm


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
        pass

    data['ingredient_form'] = form_ingredient
    data['ingredients'] = Ingredient.objects.all().order_by('-id')
    return render(request, 'kitchen/ingredient.html', data)


def createsnack(request):
    data = dict()
    product_form = ProductForm(request.POST or None)
    snack_form = ProductIngredientForm(request.POST or None)
    if product_form.is_valid() and snack_form.is_valid():
        p = product_form.save(request)
        snack_form.save(p)
        data['product_saved'] = True
        #return redirect('url_listagem')

    data['product_form'] = product_form
    data['snack_form'] = snack_form
    return render(request, 'kitchen/createsnack.html', data)
