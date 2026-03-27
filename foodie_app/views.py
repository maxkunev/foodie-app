from django.shortcuts import get_object_or_404, render, redirect

from foodie_app.forms import CategoryForm, RecipeForm
from .models import Category
from recipes.models import Recipe
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request, "foodie_app/index.html", context)

def recipes(request, category_id):
    recipes = Recipe.objects.filter(category = category_id)
    category = Category.objects.get(pk = category_id)
    context = {"recipes": recipes,
               "category": category}
    return render(request, "foodie_app/recipes.html", context)

@login_required
def add_category(request):
    
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added!")
            return redirect("foodie_app:foodie_app_home")
        else:
            return render(request, "foodie_app/add_category.html", context)
        
    else:
        form = CategoryForm()
        context = {"form": form}
        
    return render(request, "foodie_app/add_category.html", context)

@login_required
def add_recipe(request):
    new_recipe = None
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user=request.user
            new_recipe.save()
            messages.success(request, "Recipe added!")
            return redirect("recipes:recipes_home")
    
    else:
        form = RecipeForm()
 
    return render(request, "foodie_app/add_recipe.html", {"form":form})

@login_required
def add_recipe_genre(request, category_id=None):
    category = None
    initial_data = {}
    new_recipe = None
    if category_id:
        #category = Category.objects.get(pk = category_id)
        category = get_object_or_404(Category, pk = category_id)
        initial_data = {"category": category}
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, initial=initial_data)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user = request.user
            new_recipe.save()
            messages.success(request, "Recipe added!")
            return redirect('foodie_app:recipes_category', category_id = new_recipe.category.id)
    else:
        form = RecipeForm(initial=initial_data)
    
    context = {
        "form": form,
        "category": category
    }
    return render(request, 'foodie_app/add_recipe.html', context)