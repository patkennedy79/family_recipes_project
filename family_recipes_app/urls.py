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
from family_recipes_app.views import RecipesListView


urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /about
    url(r'^about/$', views.about, name='about'),
    # example: /list
    url(r'^list/$', RecipesListView.as_view(), name='recipes_list'),
    url(r'^admin/', include(admin.site.urls)),
]
