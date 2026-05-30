import pytest
from foodie_app.models import Category
from recipes.models import Recipe
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@pytest.mark.django_db
def test_create_recipe():
    
    #Arrange
    fake_author = User.objects.create(username="test_person")
    fake_category = Category.objects.create(name="Dessert")
    
    #Act
    recipe = Recipe.objects.create(
        user=fake_author,
        category=fake_category,
        name="Test cake",
        ingredients="Test ingridient",
        directions="Test direction",
        
    )
    
    #Assert
    assert recipe.category == fake_category
    assert recipe.name == "Test cake"
    assert recipe.ingredients == "Test ingridient"
    assert recipe.directions == "Test direction"

@pytest.mark.django_db
def test_delete_recipe():
    #Arrange
    fake_author = User.objects.create(username="test_person")
    fake_category = Category.objects.create(name="Dessert")
    
    #Act
    recipe = Recipe.objects.create(
        user=fake_author,
        category=fake_category,
        name="Test cake",
        ingredients="Test ingridient",
        directions="Test direction",
        
    )
    recipe.delete()
    
    #Assert
    assert Recipe.objects.count() == 0
    assert Recipe.objects.filter(pk=recipe.pk).exists() == False

