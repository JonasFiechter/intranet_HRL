from django.forms import ModelForm
from .models import *
from django_summernote.widgets import SummernoteWidget

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'img']
        widgets = {
            'description': SummernoteWidget
        }