from django.shortcuts import render, get_object_or_404, get_list_or_404
from kitchen.models import Product
from kitchen.form import ProductIngredientForm


def index(request):
    data = dict()
    data['snacks'] = get_list_or_404(Product)
    return render(request, 'kitchen/index.html', data)


def createsnack(request):
    data = dict()
    data['snack_form'] = ProductIngredientForm()
    return render(request, 'kitchen/createsnack.html', data)
