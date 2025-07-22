from django.contrib import admin
from .models import Category, Task

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'due_date', 'completed', 'created_at']
    list_filter = ['completed', 'category', 'due_date']
    search_fields = ['title']
    list_editable = ['completed']
    date_hierarchy = 'due_date'
