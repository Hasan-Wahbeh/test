"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app1.views import Home, postView, showView  ,login_view ,register_view ,Start,logout_view,GoTocommentView,CommentView,showPosts,showPostsNotLogin,GoTodeleteComment,deleteView,GoTodeletePost,deletePostView



urlpatterns = [



    path('', Home),
    path('addBlogs/', postView),
    path('addComments/', GoTocommentView),
    # path('ConfirmDelete/', deleteComment),
    path('deletePost/', GoTodeletePost),

    path('deleteComments/', GoTodeleteComment),

    path('showComment/', CommentView),
    path('deleteView/', deleteView),
    path('deletePostView/', deletePostView),


    path('showPosts/', showPosts),
    path('showPostsNotLogin/', showPostsNotLogin),

    path('showBlogs/', showView ),
    # path('showHtmlBasics/', htmlBasics),
    path('accounts/login/', login_view),
    path('accounts/logout/', logout_view),
    path('accounts/register/', register_view),
    path('admin/', admin.site.urls),


]
