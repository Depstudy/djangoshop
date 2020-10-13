from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mainapp.main, name="main"),
    path("products/", include("mainapp.urls", namespace="products")),
    path("contacts/", mainapp.contacts, name="contacts"),
    path("details/", mainapp.details, name="details"),
    path("auth/", include("authnapp.urls", namespace="auth")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
