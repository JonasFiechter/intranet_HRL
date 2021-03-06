from django.shortcuts import render, redirect
from .models import PhoneExtensions, FunctionsBySector
from app_blog.models import Post
from app_file_storage.models import Messages
from django.core.paginator import Paginator
from app_file_storage.components.files_walker import files_walker

# Create your views here.

def home_view(request):

    #  Calling the files walker function
    root_dir = r'./media'
    try:
        path = request.GET['f']
    except:
        path = ''

    dirs, files, history = files_walker(root_dir, path)

    messages_overlay = False

    posts = Post.objects.all().order_by('-id')
    posts_paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    posts = posts_paginator.get_page(page)

    messages = Messages.objects.all().order_by('-id')
    if len(messages) > 7:
        messages_overlay = True
    messages_paginator = Paginator(messages, 7)
    messages_page = request.GET.get('messages_page')
    messages = messages_paginator.get_page(messages_page)

    for message in messages:
        message.file = '/media/' + str(message.file)

    return render(request, 'app_home/home.html', {'posts': posts,
                                                  'messages': messages,
                                                  'messages_overlay': messages_overlay,
                                                  'dirs': dirs,
                                                  'files': files,
                                                  'history': history,})


def phone_extensions_view(request):
    branches = PhoneExtensions.objects.all()
    return render(request, 'phone_extensions/phone_extensions.html', {'branches': branches})


def help_me_view(request):
    functions = FunctionsBySector.objects.all()

    return render(request, 'help_me/help_me.html', {
        'functions': functions,
    })