from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    sort_param = request.GET.get('sort')

    if sort_param == 'name':
        phone_catalog = Phone.objects.order_by('name')
    elif sort_param == 'min_price':
        phone_catalog = Phone.objects.order_by('price')
    elif sort_param == 'max_price':
        phone_catalog = Phone.objects.order_by("-price")
    else:
        phone_catalog = Phone.objects.all()

    return render(request, 'catalog.html', context={'phone_catalog': phone_catalog})


def show_product(request, slug):
    phone = Phone.objects.get(slug__iexact=slug)

    return render(request, 'product.html', context={'phone': phone})
