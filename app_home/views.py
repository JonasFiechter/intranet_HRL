from django.shortcuts import render, redirect
from .models import PhoneExtensions, FunctionsBySector
from app_blog.models import Post
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
    posts = Post.objects.order_by('-id')
    paginator = Paginator(posts, 3)
    posts = paginator.get_page(request.GET.get('page'))

    return render(request, 'app_home/home.html', {'posts': posts})

def phone_extensions_view(request):
    branches = PhoneExtensions.objects.all()
    return render(request, 'phone_extensions/phone_extensions.html', {'branches': branches})

def help_me_view(request):
    functions = FunctionsBySector.objects.all()

    return render(request, 'help_me/help_me.html', {
        'functions': functions
    })