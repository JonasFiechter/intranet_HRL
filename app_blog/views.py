from functools import reduce
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from .models import *

# Create your views here.

def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'app_blog/post.html', {'post': post})


def blog_view(request):
    return render(request, 'app_blog/blog.html')


@login_required(redirect_field_name='url_login')
def blog_admin_view(request, action, post_id):

    #  Check if the group below is linked to the active user
    if request.user.groups.filter(name='GROUP-QUALIDADE').exists():
        is_valid = False
        form = PostForm(request.POST, request.FILES)
        posts = Post.objects.order_by('-id')
    
    #  In case of button delete is pressed and confirmed
    #  the confirmation step is written in a JavaScript file inside static folder
    if action == 'delete':
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            return redirect('url_blog_admin', action='blank', post_id=0)
        except:
            print('error ocurred!')

    #  In case of comming for the first time or refreshing the page
    elif action == 'blank':
        #  In case of form is valid
        if form.is_valid():
            form.save()
            is_valid = True
            message = 'Post enviado com sucesso!'
            return render(request, 'app_blog/blog_admin.html', {'is_valid': is_valid,
                                                                    'message': message,
                                                                    'form': form})

        return render(request, 'app_blog/blog_admin.html', {'form': form,
                                                            'is_valid': is_valid,
                                                            'posts': posts})
    #  In case of edit button is pressed
    if action == 'edit':
        
        edit_mode = True
        post = Post.objects.get(id=post_id)
        form = PostForm(instance=post)
        
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                is_valid = True
                message = 'Post ALTERADO com sucesso!'

                return render(request, 'app_blog/blog_admin.html', {'form': form,
                                            'is_valid': is_valid,
                                            'posts': posts,
                                            'edit_mode': edit_mode,
                                            'message': message})
            else:
                print('error')

        return render(request, 'app_blog/blog_admin.html', {'form': form,
                                                    'is_valid': is_valid,
                                                    'posts': posts,
                                                    'edit_mode': edit_mode})

    #  In case of user that does not belong to the group of user of this section
    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')
