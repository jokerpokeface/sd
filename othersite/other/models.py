from django.db import models
#from userauth.models import *
from django.contrib import admin
# Create your models here.
class Hw(models.Model):
	title = models.CharField(max_length = 50,verbose_name = 'title')
	pic = models.FileField(upload_to = 'homeworkPic',verbose_name = 'picture')
	doc = models.FileField(upload_to = 'HomeworkDoc',verbose_name = 'files')

class User(models.Model):
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
class UserAdmin(admin.ModelAdmin):
	list_display = ('username','password')



#class Informs(models.Model):
	#content = models.CharField(max_length = 150)
#class InformsAdmin(admin.ModelAdmin):
	#list_display = ('content')
#student
class Student(models.Model):
	username = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	status = models.CharField(max_length = 50)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('username','password','name','status')
#teacher
class Teacher(models.Model):
	teachername = models.CharField(max_length = 50)
	teacherpassword = models.CharField(max_length = 50)
	teacherstate = models.CharField(max_length = 50)
class TeacherAdmin(admin.ModelAdmin):
	list_display = ('teachername','teacherpassword','teacherstate')
#course
class Course(models.Model):
	name = models.CharField(max_length = 50)
	student = models.ManyToManyField(Student)
	teacher = models.ForeignKey(Teacher)

#class Post(models.Model):
	#title = models.CharField(max_length = 150)
	#body = models.TextField()
	#timestamp = models.DateTimeField()
	#course = models.ForeignKey(Course)
#class PostAdmin(admin.ModelAdmin):
	#list_display = ('title','timestamp')

class Post1(models.Model):
	body = models.TextField()
	course = models.ForeignKey(Course)
class Upfile(models.Model):
	title = models.CharField(max_length = 50)
	files = models.FileField(upload_to = 'files')
class DocFile(models.Model):
	title = models.CharField(max_length = 50)
	files = models.FileField(upload_to = 'docs')

class Prospect(models.Model):
	pro = models.TextField()
	books = models.TextField()
	course = models.ForeignKey(Course)
class Homework3(models.Model):
	name = models.CharField(max_length = 50)
 	pubDate = models.DateTimeField()
 	title = models.CharField(max_length = 50)
 	content = models.CharField(max_length = 150)
 	state = models.CharField(max_length = 50)
 	grade = models.IntegerField()
 	comment = models.TextField()
 	course = models.ForeignKey(Course)
	student = models.ManyToManyField(Student)
class Comments(models.Model):
	grade = models.IntegerField()
 	comment = models.TextField()
 	homework = models.ForeignKey(Homework3)
 	student = models.CharField(max_length = 50)
 	course = models.CharField(max_length = 50)
class Homeworkcontent(models.Model):
	content = models.TextField()
	homework = models.ForeignKey(Homework3)
class Hcontent(models.Model):
	content = models.TextField()
	homework = models.ForeignKey(Homework3)
	fromStu = models.CharField(max_length = 50)
class HomeworkFile(models.Model):
	title = models.CharField(max_length = 50)
	files = models.FileField(upload_to = 'homeworks')
	homework = models.ForeignKey(Homework3)
class TeaHomeworkFile(models.Model):
	title = models.CharField(max_length = 50)
	files = models.FileField(upload_to = 'teachhomeworks')
	homework = models.ForeignKey(Homework3)
class problem1(models.Model):
	content = models.CharField(max_length = 50)
	fromStu = models.CharField(max_length = 50)
	state = models.IntegerField()
class Answer(models.Model):
	content = models.CharField(max_length = 50)
	fromTea = models.CharField(max_length = 50)
	problem = models.ForeignKey(problem1)	
class Weekday(models.Model):
	day = models.IntegerField()
	state = models.CharField(max_length = 20)
class daycourse(models.Model):
	courseid = models.IntegerField()
class Allcourse(models.Model):
	information = models.TextField(max_length = 150)
	weektime = models.ManyToManyField(Weekday)
	courseid = models.ManyToManyField(daycourse)
class Allcourse2(models.Model):
	information = models.TextField(max_length = 150)
	weektime = models.IntegerField()
	courseid = models.IntegerField()
admin.site.register(Comments)
admin.site.register(Hcontent)
admin.site.register(Homeworkcontent)
admin.site.register(Upfile)
admin.site.register(DocFile)
admin.site.register(HomeworkFile)
admin.site.register(Homework3)
admin.site.register(Course)
admin.site.register(User,UserAdmin)
#admin.site.register(InformPost,InformPostAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
#admin.site.register(Post,PostAdmin)
admin.site.register(Post1)
admin.site.register(Prospect)
admin.site.register(problem1)
admin.site.register(Answer)
admin.site.register(Weekday)
admin.site.register(daycourse)
admin.site.register(Allcourse)
admin.site.register(Allcourse2)
admin.site.register(TeaHomeworkFile)