from django.shortcuts import render, redirect
from .models import PhoneExtensions, FunctionsBySector
from app_blog.models import Post
from django.core.paginator import Paginator

# Create your views here.

def home_view(request):
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'app_home/home.html', {'posts': posts})

def phone_extensions_view(request):
    branches = PhoneExtensions.objects.all()
    return render(request, 'phone_extensions/phone_extensions.html', {'branches': branches})

def help_me_view(request):
    functions = FunctionsBySector.objects.all()

    return render(request, 'help_me/help_me.html', {
        'functions': functions
    })