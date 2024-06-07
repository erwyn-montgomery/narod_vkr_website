from django.contrib import admin
from django.urls import path, include
from narod import views
from narod_catalogue.views import CatalogueView, LetterView, SiteView


urlpatterns = [
    path("", CatalogueView.as_view(), name="catalogue"),
    path("<str:letter>/", LetterView.as_view(), name="letter"),
    path("site/<int:id>/", SiteView.as_view(), name="site"),
]
