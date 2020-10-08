import datetime

from django.shortcuts import render


def main(request):
    title = "Interior"
    products = [
        {
            "class_prod": "tab-product-1",
            "class_base": "tab-product",
            "image_src": "tab-products/product_1.jpg",
            "image_href": "#",
            "alt": "product-1",
        },
        {
            "class_base": "tab-product",
            "image_src": "tab-products/product_2.jpg",
            "image_href": "#",
            "alt": "product-2",
        },
        {
            "class_base": "tab-product",
            "image_src": "tab-products/product_3.jpg",
            "image_href": "#",
            "alt": "product-3",
        },
        {
            "class_prod": "tab-product-4",
            "class_base": "tab-product",
            "image_src": "tab-products/product_4.jpg",
            "image_href": "#",
            "alt": "product-4",
        },
    ]
    content = {"title": title, "products": products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "Interior Products"
    links_menu = [
        {"href": "products_all", "name": "ALL", "class": "main-menu-link"},
        {"href": "products_home", "name": "HOME", "class": "main-menu-link"},
        {"href": "products_office", "name": "OFFICE", "class": "main-menu-link"},
        {"href": "products_modern", "name": "MODERN", "class": "main-menu-link"},
        {"href": "products_classic", "name": "CLASSIC", "class": "main-menu-link"},
    ]
    same_products = [
        {"image_src": "products/product_1.jpg", "alt": "product_1", "class_base": "main-product"},
        {"image_src": "products/product_2.jpg", "alt": "product_2", "class_base": "main-product", "class_prod": "main-product-2"},
        {"image_src": "products/product_3.jpg", "alt": "product_3", "class_base": "main-product"},
        {"image_src": "products/product_4.jpg", "alt": "product_4", "class_base": "main-product"},
        {"image_src": "products/product_5.jpg", "alt": "product_5", "class_base": "main-product", "class_prod": "main-product-5"},
        {"image_src": "products/product_6.jpg", "alt": "product_6", "class_base": "main-product"},
    ]
    content = {"title": title, "links_menu": links_menu, "same_products": same_products}
    return render(request, "mainapp/products.html", content)


def contacts(request):
    title = "Interior Contacts"
    visit_date = datetime.datetime.now()
    locations = [
        {"city": "Москва", "phone": "+7-888-888-8888", "email": "info@interior.ru", "address": "В пределах МКАД"},
        {"city": "Екатеринбург", "phone": "+7-777-777-7777", "email": "info_yekaterinburg@interior.ru", "address": "Близко к центру",},
        {"city": "Владивосток", "phone": "+7-999-999-9999", "email": "info_vladivostok@interior.ru", "address": "Близко к океану",},
    ]
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contacts.html", content)

def details(request):
    title = "Interior Product details"
    content = {"title": title}
    return render(request, "mainapp/details.html", content)