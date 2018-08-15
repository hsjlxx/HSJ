import uuid

import os
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.shortcuts import render,redirect


# Create your views here.
from django_redis.serializers import json

from HArtPro import settings
from user.forms import UserForm


def regist(request):
    if request.method == 'POST':
        # 读取 request.POST字典中的数据, 借助UserProfile模型保存到数据库
        # 通过ModelForm模型表单类, 验证数据并保存到数据库中
        userForm = UserForm(request.POST)
        if userForm.is_valid(): # 判断必须要字段是否都有存在数据
            userForm.save()

            return redirect('/')
        # post提交时有验证错误, 将验证错误转成json-> dict对象
        errors = json.loads(userForm.errors.as_json())
        print(errors)

    return render(request, 'user/regist.html' ,locals())

def uploadPhoto(request):

    if request.method == 'POST':
        uploadFile:InMemoryUploadedFile = request.FILES.get('photoImg')

        # 生成新的文件名
        newFileName = str(uuid.uuid4()).replace('-','')+'.' + uploadFile.name.split('.')[-1]
        # 确定生成新的文件的目录
        dirPath = os.path.join(settings.BASE_DIR,'static/users/photo/')


        return JsonResponse({'status':200,'path':'/static/users/photo/1.png'})
    return JsonResponse({'status':200,'msg':'上传失败, 目前请求只支持POST!'})