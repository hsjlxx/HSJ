"""HArtPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.core.paginator import Paginator
from django.shortcuts import render

import xadmin as admin
from art.models import Tag, Art


def toIndex(request):
    # 加载所有的分类
    # annotate 为每个tag对象增加一个字段(Count('art') 统计每类标签的个数)
    tags = Tag.objects.all()

    # locals() 将当前函数的局部变量转成字典的key-value
    # 如：
    # {'request': request, 'tags': tags}
    # 读取分类ID
    tag_id = request.GET.get('tag')


    # 加载所有文章
    if tag_id:
        arts = Art.objects.filter(tag_id=tag_id)  # exclude() 排除条件为真的数据
    else:

        arts = Art.objects.all()

    # 将文章进行分页处理
    paginator = Paginator(arts, 10)  # 分页器

    page = request.GET.get('page')
    page = int(page) if page else 1  # 读取请求参数中page参数，如果没有,默认为1
    pager = paginator.page(page)  # 获取第一页的数据

    return render(request, 'index.html', locals())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^', toIndex),
]


