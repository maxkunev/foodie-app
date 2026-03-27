from django import forms
from foodie_app.models import Category
from recipes.models import Recipe


class CategoryForm(forms.ModelForm):    
    class Meta:
        model = Category
        fields = ["name"]
        labels = {'name': 'Category name'}
        widgets = {
            'name': forms.TextInput(attrs = {'placeholder': 'your category'})
        }
        
    
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "description", "ingredients", "directions", "category", "image"]
        labels = {"name": "Recipe title", "description": "Description", "ingredients": "Ingredients", "category": "Category"}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'your description', 'rows': '5'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'your ingredients', 'rows': '5'}),
            'directions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'your directions', 'rows': '5'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }