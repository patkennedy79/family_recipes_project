from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('family_recipes_app/index.html')
    return HttpResponse(template.render())

def about(request):
    return HttpResponse("This is the ABOUT page for the Kennedy Family Recipe site.")
