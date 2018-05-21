from thu_learn import *
import os

sizeThre = 10000 #Mb
id = input('Please input user id:')
password = input('Please input user password:')



login(user_id=id, user_pass=password)#登录，读取课程数据

semester = Semester(current=True)#current=True表示当前学期，False表示以往学期

for course in semester.courses:
    path = 'learn/' + course.name
    os.makedirs(path)
    for file in course.files:
    	if file.size < sizeThre: # 下载文件大小控制，单位为Mb，一般不会超过50Mb
        	file.save(path)