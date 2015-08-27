from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^family_recipes/', include('family_recipes_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
