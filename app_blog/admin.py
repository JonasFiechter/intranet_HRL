from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title', 'date', 'author', 'description']

admin.site.register(Post, PostAdmin)