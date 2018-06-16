from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})




# def index(request):
#     return render(request, 'blog/index.html', context={
#         'title':'我的博客首页',
#         'welcome':'欢迎访问我的博客首页'
#     })
    # return HttpResponse('欢迎访问我的博客首页, 你好,小倩倩😀')