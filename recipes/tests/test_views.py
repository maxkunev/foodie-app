import pytest

from foodie_app.models import Category
from accounts.models import User
from recipes.models import Recipe

def assert_no_form_error(response):
        if response.context and "form" in response.context:
            errors = response.conext['form'].errors
            if errors:
                raise AssertionError(f'There are errors: {errors}')

@pytest.mark.django_db
def test_add_category_page_without_auth(client):
    
    response = client.get('/add_category/')
    
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')

@pytest.mark.django_db
def test_add_recipe_page_without_auth(client):
    response = client.get('/add_recipe/')
    
    assert response.status_code == 302
    assert response.url.startswith('/accounts/login/')

@pytest.mark.django_db
def test_add_category_form_with_auth(client):
    test_user = User.objects.create(username="John_test")
    
    client.force_login(test_user)
    
    form_data = {"name": "Test_category"}
    
    response = client.post('/add_category/', data=form_data)
    
    assert response.status_code == 302
    
    assert Category.objects.count() == 1
    
    my_category = Category.objects.first()
    
    assert my_category.name == "Test_category"
    
@pytest.mark.django_db
def test_add_recipe_form_with_auth(client):
    test_user = User.objects.create(username="John_test")
    
    client.force_login(test_user)
    
    test_category = Category.objects.create(name="Category_test")
    
    form_data = {
                "name": "Recipe_test", 
                "description": "Description", 
                "ingredients": "Ingredients", 
                "directions": "directions",
                "category": test_category.pk
                }
    
    response = client.post('/add_recipe/', data=form_data)
    
    assert_no_form_error(response)
    
    assert response.status_code == 302
    
    assert Recipe.objects.count() == 1
    
    my_recipe = Recipe.objects.first()
    
    assert my_recipe.name == "Recipe_test"
    assert my_recipe.category.name == "Category_test"
    
    assert my_recipe.user == test_user