from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic

from .models import Recipe


def index(request):
    template = loader.get_template('family_recipes_app/index.html')
    return HttpResponse(template.render())

def about(request):
    return HttpResponse("This is the ABOUT page for the Kennedy Family Recipe site.")

class RecipesListView(generic.ListView):
    template_name = 'family_recipes_app/recipes_list.html'
    context_object_name = 'recipes_list'

    def get_queryset(self):
        return Recipe.objects.order_by('-name')
