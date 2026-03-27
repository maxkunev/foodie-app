from django.contrib import admin

# Register your models here.

from sandbox.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    
    list_display = ("name", "email", "feedback")
    search_fields = ["email"]


    
admin.site.register(Feedback, FeedbackAdmin)