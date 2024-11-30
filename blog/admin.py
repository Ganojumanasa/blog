from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'category', 'tags')  # Fields to display in the list view
    search_fields = ('title', 'content', 'category', 'tags')  # Fields to search by in the admin interface
    list_filter = ('category', 'tags')  # Filters to apply in the admin sidebar
    
admin.site.register(BlogPost, BlogPostAdmin)
