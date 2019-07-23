from unittest import loader
import pymysql

from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import post,Comment
from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    login,
    logout

)

from .forms import UserLoginForm ,UserRegisterForm,CommentForm

def logout_view(request):
    logout(request)

    return render(request, "home.html",)


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()   #save to database
        users = User.objects.all()
        print(users.values_list('username', flat=True))

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)

def Start(request):
    return render(request, 'start.html')

def Home(request):
    if request.method == 'POST':
        print('&^' * 50)
    else:
        print('%' * 50)
    return render(request, 'home.html')

def showView(request):
    print('all user IDs are :')
    print(post.objects.values_list('userId', flat=True))
    return render(request, 'home.html')

# def htmlBasics(request):
#     return render(request, 'htmlBasics.html')

def postView(request):
    if request.method == 'POST':
        if request.POST.get('userId') and request.POST.get('title') and request.POST.get('body'):
            Post = post()
            Post.userId = request.POST.get('userId')
            Post.title = request.POST.get('title')
            Post.body = request.POST.get('body')
            Post.save()

            print('all user IDs are :')
            print(post.objects.values_list('userId', flat=True))
            print('all titles are :')
            print(post.objects.values_list('title', flat=True))

            print('*'*70)
            print(Post.id)
            print( 'the user ID is :'+ Post.userId)
            print('the title is :'+Post.title)
            print('the body is :'+Post.body)
            print('*'*65)

            return render(request,'home.html')
    else:
        print('%'*50)
        return render(request,'home.html')

def CommentView(request):

    if request.method == 'POST':
        if request.POST.get('user') and request.POST.get('email') and request.POST.get('body'):
            comment1 = Comment()
            comment1.user = request.POST.get('user')
            comment1.email = request.POST.get('email')
            comment1.body = request.POST.get('body')
            comment1.save()


            return render(request,'home.html')
    else:
        print('%'*50)
        return render(request,'home.html')

def GoTocommentView(request):
    return render(request, 'Comment.html')
