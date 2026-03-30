from django import forms
from foodie_app.models import Category
from recipes.models import Recipe
from django.core.exceptions import ValidationError
from django.db.models import Q

class CategoryForm(forms.ModelForm):    
    class Meta:
        model = Category
        fields = ["name"]
        labels = {'name': 'Category name'}
        widgets = {
            'name': forms.TextInput(attrs = {'placeholder': 'your category'})
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            cleaned_name = name.strip().capitalize()
            if Category.objects.filter(name__iexact=cleaned_name):
                raise ValidationError("This category is already exists!")
            return cleaned_name
        return name
    
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
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            cleaned_name = name.strip().capitalize()
            if Recipe.objects.filter(name__iexact=cleaned_name, user=self.user).exists():
                raise ValidationError("This recipe is already exists in your recipes!")
            return cleaned_name
        return name