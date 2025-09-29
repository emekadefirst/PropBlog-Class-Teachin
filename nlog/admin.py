from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title", "content"]



admin.site.register(Blog, BlogAdmin)