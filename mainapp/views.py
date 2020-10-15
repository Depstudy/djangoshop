from django.conf import settings
from django.shortcuts import render
from django.utils import timezone

from .models import Contact, Product, ProductCategory


def main(request):
    title = "Interior"

    products = Product.objects.all()
    
    content = {"title": title, "products": products, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "Interior Products"
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    content = {"title": title, "links_menu": links_menu, "same_products": same_products, "media_url": settings.MEDIA_URL,}
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/products.html", content)


def contacts(request):
    title = "Interior Contacts"
    visit_date = timezone.now()
    locations = Contact.objects.all()
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contacts.html", content)

def details(request):
    title = "Interior Product details"
    content = {"title": title}
    return render(request, "mainapp/details.html", content)