from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'author', 'description']

admin.site.register(Post, PostAdmin)