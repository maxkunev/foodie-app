

from django.urls import path

from djangocoursera import settings

from . import views

from django.conf.urls.static import static


app_name = "foodie_app"

urlpatterns = [
    path('', views.index, name = 'foodie_app_home'),
    path('category/<int:category_id>/', views.recipes, name = 'recipes_category'),
    path('add_category/', views.add_category, name = 'add_category'),
    path('add_recipe/', views.add_recipe, name = 'add_recipe_no_genre'),
    path('add_recipe/category/<int:category_id>', views.add_recipe_genre, name = 'add_recipe_with_genre'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
