from thu_learn import *
import os

login(user_id='', user_pass='')
semester = Semester(current=False)

for course in semester.courses:
    path = 'file/' + course.name
    os.makedirs(path)
    for file in course.files:
        file.save(path)