from django.http import HttpResponse
from django.http import JsonResponse
from .models import Recipe


# Create your views here.
def recipes_list(request):
    if 'name' in request.GET:
        recipes = Recipe.objects.filter(
            name__icontains=request.GET['name'])
    else:
        recipes = Recipe.objects.all()
    recipes_data = []
    for recipe in recipes:
        recipes_data.append({
            'id': recipe.id,
            # recipe.author is not JSON serializable
            'author': recipe.author.username,
            'name': recipe.name,
            'serves': recipe.serves,
            'time': recipe.time,
            'ingredients': recipe.ingredients,
            'procedure': recipe.procedure
        })
    # msg = ', '.join(recipe.name for recipe in recipes)
    # return HttpResponse(msg)
    return JsonResponse(recipes_data, safe=False)
