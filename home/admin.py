from django.contrib import admin
from .models import BlogPost, Category, UserProfile

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(UserProfile)
