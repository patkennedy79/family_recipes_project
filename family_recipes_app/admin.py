from django.contrib import admin

from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'recipe_type')

admin.site.register(Recipe, RecipeAdmin)
