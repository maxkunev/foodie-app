from django.shortcuts import get_object_or_404, render, redirect

from foodie_app.forms import CategoryForm, RecipeForm
from .models import Category
from recipes.models import Recipe
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from recipes.utils import get_pagination

from django.core.cache import cache

def index(request):
    
    categories = cache.get('all_categories')
    if not categories:
        categories = Category.objects.all()
        
        cache.set('all_categories', categories, 86400)
        
    context = {"categories":categories}
    return render(request, "foodie_app/index.html", context)

def recipes(request, category_id):
    recipes = Recipe.objects.with_likes().filter(category = category_id)
    category = get_object_or_404(Category, pk = category_id)
    
    sort_date = request.GET.get('sort_date', '').strip()
    sort_likes = request.GET.get('sort_likes', '').strip()
    sort_list=[]
    
    if sort_likes:
        if sort_likes == "Most_liked":
            sort_list.append("-likes_total")
        elif sort_likes == "Least_liked":
            sort_list.append("likes_total")
            
    if sort_date:
        if sort_date == "Newest":
            sort_list.append("-date_added")
        elif sort_date == "Oldest":
            sort_list.append("date_added")
        
    if sort_list:
        recipes = recipes.order_by(*sort_list)
    
    page_number = request.GET.get("page")
    page_obj, window = get_pagination(recipes, page_number)

    
    context = {
        "recipes": page_obj, 
        "category": category, 
        "result": window,
        "sort_likes": sort_likes,
        "sort_date": sort_date
        }
    
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
            messages.warning(request, "Category already exists!")
            context = {
                'form': form
            }
            return render(request, "foodie_app/add_category.html", context)
        
    else:
        form = CategoryForm()
        context = {"form": form}
        
    return render(request, "foodie_app/add_category.html", context)

@login_required
def add_recipe(request):
    new_recipe = None
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user=request.user
            new_recipe.save()
            messages.success(request, "Recipe added!")
            return redirect("recipes:recipes_home")
        else:
            messages.warning(request, "We couldn't save the recipe. Please check that you filled out the form correctly. :/")
            context = {
                'form': form
            }
            return render(request, "foodie_app/add_recipe.html", context)
    
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
        form = RecipeForm(request.POST, request.FILES, initial=initial_data, user=request.user)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user=request.user
            new_recipe.save()
            messages.success(request, "Recipe added!")
            return redirect("recipes:recipes_home")
        else:
            messages.warning(request, "We couldn't save the recipe. Please check that you filled out the form correctly. :/")
            context = {
                'form': form
            }
            return render(request, "foodie_app/add_recipe.html", context)
    else:
        form = RecipeForm(initial=initial_data)
    
    context = {
        "form": form,
        "category": category
    }
    return render(request, 'foodie_app/add_recipe.html', context)