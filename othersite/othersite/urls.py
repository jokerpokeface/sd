#coding: utf8

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'othersite.views.home', name='home'),
    # url(r'^othersite/', include('othersite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', include('other.urls')),
    url(r'^login/', include('other.urls')),
    url(r'^post/','other.views.archive'),
    url(r'^test/','other.views.courselist'),
    url(r'^inform/(A-Za-z_)+','other.views.inform'),
    url(r'^inform/','other.views.inform'),
    #url(r'^homework/','other.views.hwinform'),
    url(r'^index/','other.views.index'),#学生主页URL
    url(r'^index1/','other.views.index1'),#教师主页URL
    url(r'^teacherInform/([A-Za-z_]+)','other.views.tInform'),#教师通告页面
    #url(r'^teacherInform/inform/([A-Za-z_]+)','other.views.tInform'),
    url(r'^teacherHomework/([A-Za-z_]+)/([A-Za-z_\d]+)/upHomeworkfile','other.views.tHomework2'),
    url(r'^teacherHomework/([A-Za-z_]+)/add','other.views.tHomework4'),
    url(r'^teacherHomework/([A-Za-z_]+)/([A-Za-z_\d]+)/([A-Za-z_]+)/submit','other.views.tHomework3'),#设置
    url(r'^teacherHomework/([A-Za-z_]+)/([\d]+)','other.views.tHomework1'),
    url(r'^teacherHomework/([A-Za-z_]+)','other.views.tHomework'),
    url(r'^teacherDiscuss/([\d]+)','other.views.tDiscuss1'),#教师讨论
    url(r'^teacherDiscuss/([A-Za-z_]+)','other.views.tDiscuss'),
    url(r'^teacherCourseProspect/([A-Za-z_]+)','other.views.tCourseIn'),
    url(r'^teacherUploadFile/([A-Za-z_\d]+)/delete','other.views.tDoc1'),#上传课程资料
    url(r'^teacherUploadFile/([A-Za-z_]+)/upload','other.views.tDoc'),
    url(r'^teacherUploadFile/([A-Za-z_]+)','other.views.tDoc'),
    url(r'^teacherAddStudent/([A-Za-z_]+)/register','other.views.tAdd1'),
    url(r'^teacherAddStudent/([A-Za-z_]+)','other.views.tAdd'),#添加学生
    #url(r'^homework/','other.views.homework'),
    url(r'^courses/homework/([A-Za-z_]+)/([A-Za-z_\d]+)/upload','other.views.homeworkupload'),
    url(r'^courses/homework/([A-Za-z_]+)/([A-Za-z_\d]+)','other.views.homeworktell'),
    url(r'^courses/([A-Za-z_]+)/upload','other.views.allcourseUP'),#学生主页课程表提交
    url(r'^courses/([A-Za-z_]+)/sdiscuss','other.views.sDis'),#学生讨论区提交
    url(r'^courses/(\d)/(\d{1,2})','other.views.allcourse'),
    url(r'^courses/([A-Za-z_]+)','other.views.course'),
    url(r'^admin/', include(admin.site.urls)),#ADMIN后台
)
