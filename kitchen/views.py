from django.shortcuts import render, get_object_or_404, get_list_or_404


def index(request):
    data = dict()
    return render(request, 'kitchen/index.html', data)

