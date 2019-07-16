from unittest import loader
import pymysql

from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import post

from django.contrib.auth import (
    authenticate,
    login,
    logout

)

from .forms import UserLoginForm ,UserRegisterForm

def logout_view(request):
    logout(request)

    return render(request, "temp1.html",)


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
        user.save()
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
    return render(request, 'temp1.html')

def showView(request):
    print('all user IDs are :')
    print(post.objects.values_list('userId', flat=True))
    return render(request, 'temp1.html')

def showBranch1(request):
    return render(request, 'branch1.html')


def postView(request):
    if request.method == 'POST':
        if request.POST.get('userId') and request.POST.get('title') and request.POST.get('body'):
            Post = post()
            Post.userId = request.POST.get('userId')
            Post.title = request.POST.get('title')
            Post.body = request.POST.get('body')
            Post.save()

            #post.objects
            #post.objects.all().delete()  #to delete all data
            # return post.objects.all()

            print('all user IDs are :')
            print(post.objects.values_list('userId', flat=True))
            print('all titles are :')
            print(post.objects.values_list('title', flat=True))
            #print(post.objects.all())



            print('*'*70)
            print(Post.id)
            print( 'the user ID is :'+ Post.userId)
            print('the title is :'+Post.title)
            print('the body is :'+Post.body)
            print('*'*70)



            # num = Post.userId
            # tit = Post.title
            # bdy = Post.body

            # conn = pymysql.connect(host='localhost',
            #                        user='root',
            #                        password='hasan1152064',
            #                        db='new_schema',
            #                        charset='utf8mb4',
            #                        cursorclass=pymysql.cursors.DictCursor)
            #
            # with conn.cursor() as cursor:
            #     sql  = "INSERT INTO `new_schema`.`blogs` (`blogId`,`blogTitle`,`blogBody`) VALUES(20,'sdsds','hasanWahbeh')"
            #     sql2 = "INSERT INTO `new_schema`.`blogs` (`blogId`,`blogTitle`,`blogBody`) VALUES({},'{}','{}')".format(num, tit, bdy)
            #
            #     cursor.execute(sql2)
            #     conn.commit()

            return render(request,'temp1.html')
    else:
        print('%'*50)
        return render(request,'temp1.html')
