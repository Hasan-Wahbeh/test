from unittest import loader
import pymysql

from django.http import HttpResponse
from django.shortcuts import render
from .models import post


def Home(request):
    if request.method == 'POST':
        print('&^' * 50)
    else:
        print('%' * 50)
    return render(request, 'temp1.html')


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
