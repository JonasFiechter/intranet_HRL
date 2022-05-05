from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from .models import *

# Create your views here.

# def single_post_view(request):
#     return render(request, 'HTML HERE')

@login_required(redirect_field_name='url_login')
def blog_admin_view(request, action, post_id):

    posts = Post.objects.order_by('-id')
    
    #  In case of button delete is pressed and confirmed
    #  the confirmation step is written in a JavaScript file inside static folder
    if action == 'delete':
        try:
            post = Post.objects.get(id=post_id)
            post.delete()
            print('success!')

        except:
            print('error ocurred!')

    #  Check if the group below is linked to the active user
    if request.user.groups.filter(name='GROUP-ENGENHARIA').exists():
        is_valid = False
        form = PostForm(request.POST, request.FILES)

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

    else:
        messages.error(request, message='Você não tem permissão para acessar esta sessão!')
        return redirect('url_dashboard')
