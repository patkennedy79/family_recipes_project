from random import random

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.shortcuts import render

from .models import Recipe


def index(request):
    template = loader.get_template('family_recipes_app/index.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('family_recipes_app/about.html')
    return HttpResponse(template.render())

def whats_for_dinner(request):
    dinner_recommendation_found = False
    all_recipes = Recipe.objects.all()
    dinner_recipes = Recipe.objects.filter(recipe_type=Recipe.DINNER)

    if dinner_recipes.count() > 0:
        while not dinner_recommendation_found:
            proposed_index = int((random() * 1000) % all_recipes.count()) + 1
            proposed_recipe = Recipe.objects.get(id=proposed_index)

            if proposed_index % 10 == 0:
                proposed_recipe.name = "TAKEOUT"

            if proposed_recipe.recipe_type == Recipe.DINNER:
                dinner_recommendation_found = True

        dinner_recommendation = proposed_recipe

    context = {'dinner_recommendation': dinner_recommendation}
    return render(request, 'family_recipes_app/whats_for_dinner.html', context)

class RecipesListView(generic.ListView):
    template_name = 'family_recipes_app/recipes_list.html'
    context_object_name = 'recipes_list'

    def get_queryset(self):
        return Recipe.objects.order_by('-name')

class BreakfastRecipesListView(generic.ListView):
    template_name = 'family_recipes_app/recipe_type_list.html'
    context_object_name = 'recipe_type_list'

    def get_queryset(self):
        return Recipe.objects.filter(recipe_type=Recipe.BREAKFAST)

class LunchRecipesListView(generic.ListView):
    template_name = 'family_recipes_app/recipe_type_list.html'
    context_object_name = 'recipe_type_list'

    def get_queryset(self):
        return Recipe.objects.filter(recipe_type=Recipe.LUNCH)

class DinnerRecipesListView(generic.ListView):
    template_name = 'family_recipes_app/recipe_type_list.html'
    context_object_name = 'recipe_type_list'

    def get_queryset(self):
        return Recipe.objects.filter(recipe_type=Recipe.DINNER)

class DessertRecipesListView(generic.ListView):
    template_name = 'family_recipes_app/recipe_type_list.html'
    context_object_name = 'recipe_type_list'

    def get_queryset(self):
        return Recipe.objects.filter(recipe_type=Recipe.DESSERT)

class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'family_recipes_app/recipe_detail.html'
