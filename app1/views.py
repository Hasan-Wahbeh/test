from unittest import loader
import pymysql
from django.shortcuts import get_list_or_404, get_object_or_404

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
    posts = post.objects.all()
    comments = Comment.objects.all()
    Users = User.objects.all()
    args = {'posts': posts, 'comments': comments, 'Users': Users}

    if request.method == 'POST':
        print('&^' * 50)
    else:
        print('%' * 50)
    return render(request, 'home.html',args)

def showView(request):

    print('all user IDs are :')
    print(post.objects.values_list('userId', flat=True))
    return render(request, 'home.html')

def showPostsNotLogin(request):
    posts = post.objects.all()
    comments = Comment.objects.all()
    args = {'posts': posts, 'comments': comments}

    return render(request, 'allPostsNotLogin.html', args)


def showPosts(request):
    posts = post.objects.all()
    comments = Comment.objects.all()
    Users = User.objects.all()
    args = {'posts': posts , 'comments' : comments , 'Users' : Users}

    return render(request, 'allPosts.html',args)


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
            commUser=request.POST.get('user')
            commEmail=request.POST.get('email')
            commBody=request.POST.get('body')
            commPost=request.POST.get('post')
            comment1.user = commUser
            comment1.email = commEmail
            comment1.body = commBody
            comment1.post_id=commPost
            # p1=post(commUser,commEmail,commBody)
            # p1.save()
            # comment1.save()
            # comment1.post_id.add(p1)
            # comment1.postrelation.many_to_many(p1)
            # comment1.post_id= post.objects.exists()
            # print(request.POST.get('system', None))
            # comment1.post_id = 1
            comment1.save()

            posts = post.objects.all()
            comments = Comment.objects.all()
            Users = User.objects.all()
            args = {'posts': posts, 'comments': comments, 'Users': Users}

            return render(request,'home.html',args)
    else:
        print('%'*50)
        return render(request,'home.html')

def GoTocommentView(request):
    posts = post.objects.all()
    comments = Comment.objects.all()
    Users = User.objects.all()
    post_id = request.POST.get('post_id', None)
    args = {'post_id': post_id,'posts': posts, 'comments': comments, 'Users': Users}

    return render(request, 'comment.html',args)

def GoToPostView(request):
     return render(request, 'Post.html')

def GoTodeleteComment(request):
    context = {}
    commentId = request.POST.get('commentId', None)
    context['commentId'] = commentId
    # postId = request.POST.get('postId', None)
    # context['postId'] = postId

    return render(request, 'deletecomment.html', context)

def GoTodeletePost(request):
    context = {}
    postId = request.POST.get('postId', None)
    context['postId'] = postId
    # postId = request.POST.get('postId', None)
    # context['postId'] = postId

    return render(request, 'deletepost.html', context)

def deleteView(request):
    id = request.POST.get('commentId')
    # pk = request.POST.get('PostId')
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=id,pk=id)
        comment.delete()
        print(comment.body)
        print( 'You have successfully deleted the comment')


    posts = post.objects.all()
    comments = Comment.objects.all()
    Users = User.objects.all()
    args = {'posts': posts, 'comments': comments, 'Users': Users}

    return render(request, 'allPosts.html', args)


def deletePostView(request):
    id = request.POST.get('postId')
    # pk = request.POST.get('PostId')
    if request.method == 'POST':
        post1 = get_object_or_404(post, id=id,pk=id)
        post1.delete()
        print(post1.body)
        print( 'You have successfully deleted the Post')


    posts = post.objects.all()
    comments = Comment.objects.all()
    Users = User.objects.all()
    args = {'posts': posts, 'comments': comments, 'Users': Users}

    return render(request, 'allPosts.html', args)

