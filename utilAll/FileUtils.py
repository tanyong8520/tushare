# -*- coding: utf-8 -*-
import os


def handle_upload_file(file,filename):
    path='media/uploads/'     #上传文件的保存路径，可以自己指定任意的路径
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path+filename,'wb+')as destination:
        for chunk in file.chunks():
            destination.write(chunk)