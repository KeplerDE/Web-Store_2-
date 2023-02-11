# функции = контроллеры = вьюхи
from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'Test Title',
        'username': 'Anton',

    }
    return render(request, 'products\index.html', context)  # передать контекст обязательно


def products(request):

    context = {
        'title': 'Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products\products.html', context)    # дублировать строки CTRL + D