"""family_recipes_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from . import views
from family_recipes_app.views import RecipesListView, RecipeDetail, BreakfastRecipesListView, LunchRecipesListView, DinnerRecipesListView, DessertRecipesListView


urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /about/
    url(r'^about/$', views.about, name='about'),
    # example: /recipes/
    url(r'^recipes/$', RecipesListView.as_view(), name='recipes_list'),
    # example: /recipes/03/
    url(r'^recipes/(?P<pk>[0-9]+)/$', RecipeDetail.as_view(), name='recipe_detail'),
    # example: /recipes/breakfast/
    url(r'^recipes/breakfast/$', BreakfastRecipesListView.as_view(), name='breakfast_recipes_list'),
    # example: /recipes/dinner/
    url(r'^recipes/lunch/$', LunchRecipesListView.as_view(), name='lunch_recipes_list'),
    # example: /recipes/dinner/
    url(r'^recipes/dinner/$', DinnerRecipesListView.as_view(), name='dinner_recipes_list'),
    # example: /recipes/dessert/
    url(r'^recipes/dessert/$', DessertRecipesListView.as_view(), name='dessert_recipes_list'),
    # example: /recipes/whats_for_dinner/
    url(r'^recipes/whats_for_dinner/$', views.whats_for_dinner, name='whats_for_dinner'),
    # example: /admin/
    url(r'^admin/', include(admin.site.urls)),
]
