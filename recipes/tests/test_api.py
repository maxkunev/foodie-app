import pytest

from rest_framework.test import APIClient

from accounts.models import User
from foodie_app.models import Category
from recipes.models import Recipe

@pytest.mark.django_db
def test_get_recipes_anonymous():
    api_client = APIClient()

    fake_author = User.objects.create(username="test_person")
    fake_category = Category.objects.create(name="Dessert")

    recipe = Recipe.objects.create(
        user=fake_author,
        category=fake_category,
        name="Test cake",
        ingredients="Test ingridient",
        directions="Test direction",
        
    )
    
    response = api_client.get(
        '/recipes/api/recipes/',       
        format='json'    
    )
    response_data = response.data[0]
    assert response.status_code == 200
    assert response_data["id"] == recipe.pk
    

@pytest.mark.django_db
def test_create_recipe_anonymous():
    api_client = APIClient()
    category = Category.objects.create(name="Dessert_test_api")
    test_user = User.objects.create(username="api_tester")
    
    my_form_data = {
            "name": "Test_api_recipe_creation",
            "description": "string",
            "ingredients": "string",
            "category": category.pk,
            "user": test_user.pk
    }
    
    response = api_client.post(
        '/recipes/api/recipes/',       
        data=my_form_data,    
        format='json'          
    )
    
    assert response.status_code == 403



@pytest.mark.django_db
def test_create_recipe_with_auth():
    api_client = APIClient()
    test_user = User.objects.create(username="api_tester")
    category = Category.objects.create(name="Dessert_test_api")
    api_client.force_authenticate(user=test_user)
    
    my_form_data = {
            "name": "Test_api_recipe_creation",
            "description": "string",
            "ingredients": "string",
            "category": category.pk,
            "user": test_user.pk
    }
    
    response = api_client.post(
        '/recipes/api/recipes/',       
        data=my_form_data,    
        format='json'          
    )
    
    assert response.status_code == 201
    assert Recipe.objects.count() == 1
    
    my_recipe = Recipe.objects.first()
    
    assert my_recipe.name == "Test_api_recipe_creation"
    assert my_recipe.category.name == "Dessert_test_api"
    
    assert my_recipe.user == test_user
    
@pytest.mark.django_db
def test_api_delete_recipe_anonymous():
    api_client = APIClient()

    fake_author = User.objects.create(username="test_person")
    fake_category = Category.objects.create(name="Dessert")

    recipe = Recipe.objects.create(
        user=fake_author,
        category=fake_category,
        name="Test cake",
        ingredients="Test ingridient",
        directions="Test direction",
        
    )

    
    response = api_client.delete(
        f'/recipes/api/recipes/{recipe.pk}/',       
        format='json'
    )

    assert response.status_code == 403
    
    
@pytest.mark.django_db
def test_api_delete_recipe_with_auth():
    api_client = APIClient()

    fake_author = User.objects.create(username="test_person")
    fake_category = Category.objects.create(name="Dessert")
    api_client.force_authenticate(user=fake_author)
    recipe = Recipe.objects.create(
        user=fake_author,
        category=fake_category,
        name="Test cake",
        ingredients="Test ingridient",
        directions="Test direction",
        
    )

    response = api_client.delete(
        f'/recipes/api/recipes/{recipe.pk}/',       
        format='json'
    )

    assert response.status_code == 204