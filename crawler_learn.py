# -*- coding: utf-8 -*-
from thu_learn import *
import os

sizeThre = 1000 #Mb

login()#登录，读取课程数据

semester = Semester(current=True)#current=True表示当前学期，False表示以往学期

for course in semester.courses:
    path = 'learn/' + course.name
    if not os.path.exists(path):
        os.makedirs(path)
    materialPath = path + '/materials/'
    if not os.path.exists(materialPath):
        os.makedirs(materialPath)
    workPath = path+'/works/'       
    if not os.path.exists(workPath):
        os.makedirs(workPath)

    for file in course.files:
        if file.size < sizeThre: # 下载文件大小控制，单位为Mb，一般不会超过50Mb
            file.save(materialPath)

    for work in course.works:
        if not work.answer is None:
            work.answer.save(workPath)
        if not work.file is None:
            work.file.save(workPath)
