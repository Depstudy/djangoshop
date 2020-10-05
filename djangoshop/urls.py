from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mainapp.main, name="main"),
    path("products/", mainapp.products, name="products"),
    path("contacts/", mainapp.contacts, name="contacts"),
    path("details/", mainapp.details, name="details"),
]
