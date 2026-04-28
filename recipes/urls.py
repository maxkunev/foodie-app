from django.urls import include, path
from recipes import views

from rest_framework.routers import DefaultRouter

app_name = "recipes"

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet, basename="recipes")

urlpatterns = [
    path('', views.recipes, name = 'recipes_home'),
    path('<int:recipe_id>/', views.recipe_detail, name = 'recipe_details'),
    path('search/', views.search_results, name="search_results"),
    path('<int:recipe_id>/toggle_favorite/', views.toggle_favorite, name="toggle_favorite"),
    path('favorite_recipes/', views.favorite_recipes, name="favorite_recipes"),
    path('<int:recipe_id>/delete/', views.delete_recipe, name="delete_recipe"),
    path('<int:recipe_id>/edit/', views.edit_recipe, name="edit_recipe"),
    path('my_recipes/', views.my_recipes, name="my_recipes"),
    path('profile/<int:user_id>/', views.public_profile, name = 'public_profile'),
    path('api/', include(router.urls)),
    path('<int:recipe_id>/toggle_liked/', views.toggle_liked, name="toggle_liked")
]
