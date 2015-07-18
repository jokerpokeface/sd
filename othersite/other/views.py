# Create your views here.
 #coding=utf-8 
import csv
import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import Template,Context,loader
from django.http import HttpResponse,Http404
from django.http import HttpResponseRedirect
from other.models import *
from django import forms
from django.views.decorators.csrf import csrf_exempt
from other.form import * 

@csrf_exempt

#登录需要两个表格
class UserForm(forms.Form):
	username = forms.CharField(label = '名字',max_length = 100)
	password = forms.CharField(label = '密码',widget = forms.PasswordInput())
def archive(request):
	posts = InformPost.objects.all()
	t = loader.get_template("archive.html")
	c = Context({'posts':posts})
	return HttpResponse(t.render(c))
def courselist(request):
	courses = Course.objects.all()
	t = loader.get_template("courselist.html")
	c = Context({'courses':courses})
	return HttpResponse(t.render(c))
	#登录
def login(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			user = Student.objects.filter(username = username,password = password)
			if user:
				response = HttpResponseRedirect('/index/')
				response.set_cookie('username',username,36000)
				return response
			else:
				newuser = Teacher.objects.filter(teachername = username,teacherpassword = password)
				if newuser:
					response = HttpResponseRedirect('/index1/')
					response.set_cookie('username',username,36000)
					return response
				else:
					return HttpResponseRedirect('/login/')
	else:
		uf = UserForm()
	return render_to_response('login1.html',{'uf':uf})
	#学生主页
def index(request):
	courses = ['sb','sb1']
	username = request.COOKIES.get('username','')
	user = Student.objects.get(username = username)
	if user:
		courses = user.course_set.all()
	return render_to_response('StudentIndex.html',{'username':username,'courses':courses})
	#老师主页
def index1(request):
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	if teacher:
		courses = teacher.course_set.all()
	if request.method == 'POST':
		name = request.POST['coursename']
		i = Course(name = name,teacher = teacher)
		i.save()
	return render_to_response('teacherManager.html',{'courses':courses})
	#课程主页
def course(request,offset):
	try:
		offset = offset
	except ValueError:
		raise Http404()
	username = request.COOKIES.get('username','')
	course = Course.objects.get(name = offset)
	problems = problem1.objects.all()
	answers = Answer.objects.all()
	homeworks = course.homework3_set.all()
	homeworkneed = []
	for homework in homeworks:
		students = homework.student.all()
		for student in students:
			if student.name == username:
				homeworkneed.append(homework)
	posts = course.post1_set.all()
	prospects = course.prospect_set.all()
	return render_to_response('StudentCourse.html',
		{'homeworks':homeworks,'coursename':offset,
		'course':course,'posts':posts,
		'prospects':prospects,'problems':problems,
		'answers':answers})
	#学生主页自助课程表建立函数
def allcourseUP(request,offset):
	username = request.COOKIES.get('username','')
	course = Course.objects.get(name = offset)
	problems = problem1.objects.all()
	answers = Answer.objects.all()
	homeworks = course.homework3_set.all()
	homeworkneed = []
	for homework in homeworks:
		students = homework.student.all()
		for student in students:
			if student.name == username:
				homeworkneed.append(homework)
	posts = course.post1_set.all()
	prospects = course.prospect_set.all()
	row = 7
	col = 6
	if request.method == 'POST':
		for i in range(0,8):
			for j in range(0,7):
				temp = "row"+i+"col"+j
				name = request.POST[temp]
				with open('egg2.csv', 'wb') as csvfile:
					spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
					spamwriter.writerow(name)
	return render_to_response('StudentCourse.html',
		{'homeworks':homeworks,'coursename':offset,
		'course':course,'posts':posts,
		'prospects':prospects,'problems':problems,
		'answers':answers})
	#登出，暂时还没写
def logout(request):
	response = HttpResponse('logout')
	response.delete_cookie('username')
	return response
#test
def inform(request):
	content = 'sb'
	question = 'aaaa'
	if request.method == 'POST':
		question = request.POST['content']
		i = problem(content = question,fromStu = 'dasdas')
		i.save()
	return render_to_response('inform.html',{'content':question})
#讨论区
def sDis(request,offset):
	print offset
	username = request.COOKIES.get('username','')
	question = 'dic'
	if request.method == 'POST':
		question = request.POST['content']
		print question
		i = problem1(content = question,fromStu = username,state = 0)
		i.save()
	course = Course.objects.get(name = offset)
	homeworks = course.homework3_set.all()
	answers = Answer.objects.all()
	posts = course.post1_set.all()
	problems = problem1.objects.all()
	prospects = course.prospect_set.all()
	return render_to_response('StudentCourse.html',
		{'homeworks':homeworks,'coursename':offset,
		'course':course,'coursename':offset,'posts':posts,'prospects':prospects,
		'question':question,'problems':problems,'answers':answers})
#学生点击进入查看详细信息函数
def homeworktell(request,offset1,offset2):
	needstate = 1
	offset1 = offset1
	offset2 = offset2
	needid = int(offset2)
	homeworkneed = Homework3()
	homeworkchange = Homework3()
	username = request.COOKIES.get('username','')
	#student = Student.objects.get(username = username)
	course = Course.objects.get(name = offset1)
	title = 'sb'
	content = 'youasb'
	shomework = Homework3.objects.get(id = needid)
	shomework.state = 1
	shomework.save()
	return render_to_response('studentHomework.html',{'homework':shomework,'coursename':offset1})	
def homeworkupload(request,offset1,offset2):
	needstate = 1
	offset1 = offset1
	offset2 = offset2
	needid = int(offset2)
	homeworkneed = Homework3()
	homeworkchange = Homework3()
	username = request.COOKIES.get('username','')
	#student = Student.objects.get(username = username)
	course = Course.objects.get(name = offset1)
	title = 'sb'
	content = 'youasb'
	shomework = Homework3.objects.get(id = needid)
	shomework.state = 0
	shomework.save()
	needcomments = []
	ncomments = []
	allcomments = Comments.objects.all()
	for allcomment in allcomments:
		if allcomment.homework == shomework:
			needcomments.append(allcomment)
	if needcomments:
		for needcomment in needcomments:
			if needcomment.student == username:
				ncomments.append(needcomment)
	else:
		i = Comments(grade = 0,comment = '',homework = shomework,student = username,course = offset1)
		i.save()
		ncomments.append(i)
	if request.method == 'POST':
		content = request.POST['content']
		homeworkchange = Homework3.objects.get(id = offset2)
		homeworkchange.state = 0
		homeworkchange.save()
		p = Hcontent(content = content,homework = homeworkchange,fromStu = username)
		p.save()
	return render_to_response('studentHomework.html',{'homework':homeworkchange,'coursename':offset1,
		'comments':needcomment})
#老师通知函数
def tInform(request,offset):
	content = 'sb'
	coursename = offset
	course = Course.objects.get(name = coursename)
	posts = course.post1_set.all()
	if request.method == 'POST':
		content = request.POST['content']
		i = Post1(body = content,course = course)
		i.save()
		#form = InformsForm({'content':content})
		#test = form.save(commit = False)
		#test.save()
		#if form.is_valid():
			#form.save()
	return render_to_response('teacherInform.html',{'coursename':coursename,'posts':posts})
#老师发布作业函数
def tHomework(request,offset):
	Homework3.objects.order_by("pubDate")
	coursename = offset
	courses = Course.objects.get(name = coursename)
	homeworks = courses.homework3_set.all()
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	if teacher:
		courses = teacher.course_set.all()
	return render_to_response('teacherHomework.html',{'coursename':coursename,
		'homeworks':homeworks})

def tHomework1(request,offset1,offset2):
	Homework3.objects.order_by("pubDate")
	coursename = offset1
	homeworkid = offset2
	courses = Course.objects.get(name = coursename)
	homeworks = courses.homework3_set.all()
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	if teacher:
		courses = teacher.course_set.all()
	homeworks1 = Homework3.objects.get(id = homeworkid)
	students = homeworks1.student.all()

	homeworkcontents = homeworks1.hcontent_set.all()
	return render_to_response('teacherHomework.html',{'coursename':coursename,'homeworks1':homeworks1,
		'students':students,'homeworkid':homeworkid,'homeworks':homeworks,'hcontents':homeworkcontents})
#设置
def tHomework2(request,offset1,offset2):
	Homework3.objects.order_by("pubDate")
	coursename = offset1
	homeworkid = offset2
	courses = Course.objects.get(name = coursename)
	homeworks = courses.homework3_set.all()
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	courses = teacher.course_set.all()
	homeworks1 = Homework3.objects.get(id = homeworkid)
	students = homeworks1.student.all()
	if request.method == 'POST':
		content = request.POST['content']
		title = request.POST['title']
		files = request.FILES['file']
		homeworks1.content = content
		homeworks1.title = title
		homeworks1.save()#修改作业内容并保存
		i = TeaHomeworkFile(title = 'sb2',files = files,homework = homeworks1)
		i.save()
	return render_to_response('teacherHomework.html',{'coursename':coursename,'homeworks1':homeworks1,
		'students':students,'homeworks':homeworks})
#批改
def tHomework3(request,offset1,offset2,offset3):
	Homework3.objects.order_by("pubDate")
	coursename = offset1
	homeworkid = offset2
	courses = Course.objects.get(name = coursename)
	homeworks = courses.homework3_set.all()
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	ncomment = []
	if teacher:
		courses = teacher.course_set.all()
	homeworks1 = Homework3.objects.get(id = homeworkid)
	students = homeworks1.student.all()
	if request.method == 'POST':
		grade = request.POST['grade']
		comment = request.POST['comment']
		homeworks1.grade = grade
		homeworks1.comment = comment
		needcomments = []
		allcomments = Comments.objects.all()
		for allcomment in allcomments:
			if allcomment.homework == homeworks1:
				needcomments.append(allcomment)
		if needcomments:
			for needcomment in needcomments:
				if needcomment:
					needcomment.comment = comment
					needcomment.grade = grade
					needcomment.student = offset3
					needcomment.save()
					ncomment.append(needcomment)
		homeworks1.state = 2
		homeworks1.save()
	return render_to_response('teacherHomework.html',{'coursename':coursename,'homeworks1':homeworks1,
		'students':students,'homeworks':homeworks,'comments':ncomment})

def tHomework4(request,offset1):
	Homework3.objects.order_by("pubDate")
	coursename = offset1
	course_ = Course.objects.get(name = coursename)
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	now = datetime.datetime.now()
	courses = teacher.course_set.all()
	if request.method == 'POST':
		name = request.POST['name']
		content = request.POST['content']
		title = request.POST['title']
		i = Homework3(name = name,title = title,content = content,pubDate = now,
			state = 1,grade = 0,course = course_)
		i.save()
	homeworks = course_.homework3_set.all()
	return render_to_response('teacherHomework.html',{'coursename':coursename,
		'homeworks':homeworks})

#讨论
def tDiscuss(request,offset):
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	if teacher:
		courses = teacher.course_set.all()
	problems = problem1.objects.all()
	if request.method == 'POST':
		content = request.POST['answer']
		print content
		for problem in problems:
			if problem.id == offset:
				problem.state = 1
				print offset
				problem.save()
				i = Answer(content = content,fromTea = username,problem = problem)
				i.save()
	return render_to_response('teacherDiscussionArea.html',{'courses':courses,'problems':problems})

def tDiscuss1(request,offset):
	offset = int(offset)
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	if teacher:
		courses = teacher.course_set.all()
	problems = problem1.objects.all()
	if request.method == 'POST':
		content = request.POST['answer']
		print content
		problem_ = problem1.objects.get(id = offset)
		problem_.state = 1
		problem_.save()
		i = Answer(content = content,fromTea = username,problem = problem_)
		print i.id
		print i.problem
		print i.content
		print i.fromTea
		i.save()
	return render_to_response('teacherDiscussionArea.html',{'courses':courses,'problems':problems})

#课程前景
def tCourseIn(request,offset):
	coursename = offset
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	if teacher:
		courses = teacher.course_set.all()
	course = Course.objects.get(name = coursename)
	if request.method == 'POST':
		pro = request.POST['pro']
		books = request.POST['books']
		i = Prospect(pro = pro,books = books,course = course)
		i.save()
	return render_to_response('teacherCourseProspect.html',{'courses':courses})
#课程资料文件上传后的响应函数
def tDoc1(request,offset):
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	p = DocFile.objects.get(id = offset)
	p.delete()
	files = DocFile.objects.all()
	if teacher:
		courses = teacher.course_set.all()
	if request.method == 'POST':
		files = request.FILES['file']
		i = DocFile(title = 'sb',files = files)
		i.save()
	return render_to_response('teacherUploadFile.html',{'courses':courses,'files':files})
#上传资料
def tDoc(request,offset):
	print request.FILES
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	files = DocFile.objects.all()
	if teacher:
		courses = teacher.course_set.all()
	if request.method == 'POST':
		files = request.FILES['file']
		i = DocFile(title = 'sb',files = files)
		i.save()
	return render_to_response('teacherUploadFile.html',{'courses':courses,'files':files})
def tAdd(request,offset):
	print request.FILES
	coursename = offset
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	if teacher:
		courses = teacher.course_set.all()
	course = Course.objects.get(name = coursename)
	if request.method == 'POST':
		files = request.FILES['file']
		i = Upfile(title = 'sb',files = files)
		i.save()
		form = UploadFileForm(request.POST,request.FILES)
		#if form.is_valid():
			#handle_uploaded_file(request.FILES['file'])
			#return HttpResponseRedirect('/index')
		#else:
		return render_to_response('teacherAddStudent.html',{'form':form})
	return render_to_response('teacherAddStudent.html',{'coursename':coursename,'courses':courses})
def tAdd1(request,offset):
	print request.FILES
	coursename = offset
	username = request.COOKIES.get('username','')
	teacher = Teacher.objects.get(teachername = username)
	if teacher:
		courses = teacher.course_set.all()
	course = Course.objects.get(name = coursename)
	if request.method == 'POST':
		studentusername = request.POST['username']
		studentname = request.POST['name']
		studentpassword = request.POST['password']
		i = Student(username = studentusername,name = studentname,password = studentpassword,status = 0)
		i.save()
		course.student.add(i)
		#if form.is_valid():
			#handle_uploaded_file(request.FILES['file'])
			#return HttpResponseRedirect('/index')
		#else:
		return render_to_response('teacherAddStudent.html',{'coursename':coursename})
	return render_to_response('teacherAddStudent.html',{'coursename':coursename,'courses':courses})

def allcourse(request,offset1,offset2):
	o1 = 2
	o2 = 3
	o1 = int(offset1)
	o2 = int(offset2)
	courses = []
	#course1s = Allcourse2.objects.get(weektime = 1,courseid = 1)
	#if course1s:
		#return render_to_response('archive.html',{'day':o1,'courseid':o2,'course1s':course1s})
	course1s = Allcourse2.objects.all()
	for course1 in course1s:
		if course1.weektime == 1:
			if course1.courseid == 1:
				courses.append(course1)
	return render_to_response('archive.html',{'day':o1,'courseid':o2,'courses':courses})
#   def hwinform(request):
#	if request.method == 'POST':
#		form = hwinform(request.POST or None,request.FILES)
#		if form.is_valid():
#			form.save()
#	return render_to_response('upload.html')