from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import HttpResponse

from recipes.serializers import RecipeReadSerializer, RecipeWriteSerializer
# Create your views here.
from .models import Recipe
from django.db.models import Q
from foodie_app.models import Category
from foodie_app.forms import RecipeForm
from comments.forms import CommentForm
from accounts.models import UserProfile

from rest_framework import viewsets

from django.contrib.auth.decorators import login_required


def recipes(request):
    # recipes = Recipe.objects.filter(category__name__iexact = "soup")
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipes/recipes.html", context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    comments = recipe.comments.all()
    
    new_comment = None
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.user = request.user
            new_comment.save()
            return redirect(recipe.get_absolute_url())
    else:
        comment_form = CommentForm()
        
    context = {"recipe": recipe, "comments": comments, "comment_form": comment_form}
    return render(request, "recipes/recipe.html", context)

def search_results(request):
    query = request.GET.get('query', '')
    
    results = Recipe.objects.filter(
        Q(name__icontains=query) | 
        Q(description__icontains=query) | 
        Q(ingredients__icontains=query) | 
        Q(category__name__icontains=query)) if query else []
    
    seen_ids = set()
    unique_results = []

    for result in results:
        if result.id not in seen_ids:
            unique_results.append(result)
            seen_ids.add(result.id)
            
    
    context={
        "recipes":unique_results, 
        "query":query,
        }
    return render(request, "recipes/search_results.html", context)

@login_required
def toggle_favorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    
    if request.user in recipe.favorited_by.all():
        recipe.favorited_by.remove(request.user)
    else:
        recipe.favorited_by.add(request.user) 
            
    return redirect("recipes:recipe_details", recipe_id)

@login_required
def favorite_recipes(request):
    user = request.user
    recipes = user.favorite_recipes.all()
    context = {"recipes": recipes}
    return render(request, "recipes/favorite_recipes.html", context)

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if not request.user == recipe.user and not request.user.is_superuser:
        return HttpResponseForbidden()
    if request.method == "POST":
        recipe.delete()
        return redirect("recipes:my_recipes")
    
    return render(request, "recipes/recipe_confirmation_delete.html", {"recipe":recipe})

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if not request.user == recipe.user and not request.user.is_superuser:
        return HttpResponseForbidden()
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipes:recipe_details", recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
        
    context={
        "form": form,
        "recipe":recipe
             }
        
    return render(request, "recipes/recipe_form.html", context)

@login_required
def my_recipes(request):
    recipes = request.user.recipes.all()
    context = {
        "recipes":recipes
    }
    return render(request, "recipes/my_recipes.html", context)


def public_profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user__id = user_id)
    context = {
        "user_profile": user_profile
    }
    return render(request, "recipes/public_profile.html", context)

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            serializer_class = RecipeReadSerializer
            return serializer_class
    
        serializer_class = RecipeWriteSerializer
        return serializer_class
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
    