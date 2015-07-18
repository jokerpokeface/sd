from django.conf.urls import patterns, url
from other import views

 
urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
)