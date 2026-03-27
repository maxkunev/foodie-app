from django.contrib import admin
from .models import Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    
    list_display = ("id", "name", "date_added")
    search_fields = ["name"]
    


admin.site.register(Recipe, RecipeAdmin)