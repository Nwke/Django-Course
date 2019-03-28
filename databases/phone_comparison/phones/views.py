from django.shortcuts import render
from .models import Apple, Samsung


def show_catalog(request):
    apple_phones = Apple.objects.all()
    samsung_phones = Samsung.objects.all()
    return render(
        request,
        'catalog.html',
        context={'apple_phones': apple_phones, 'samsung_phones': samsung_phones}
    )
