from django.urls import path,include
from . import views

urlpatterns = [
    path(r'', views.index),
    path(r'<int:num>/', views.detail, name='num'),
    path('grades/', views.grades, name = 'grades'),
    path('students/', views.students, name = 'students'),
    path('addstudents/', views.addstudents, name = 'addstudents'),
    path('grades/<int:number>', views.gradesStudents, name = 'number'),

    # GET
    path('attribute', views.attribute, name='attribute'),
    path('attribute/get1', views.get1, name='get1'),
    path('attribute/get2', views.get2, name='get2'),

    # POST
    path('post/showregist/', views.showregist, name='showregist'),
    path('post/showregist/register/', views.register, name='register'),

    # RESPONSE
    path('response/showresponse/', views.showresponse, name='showresponse'),
    # cookie
    path('response/cookietest/', views.cookietest, name='cookietest'),

    # 重定向
    path('redirect1/', views.redirect1, name='redirect1'),
    path('redirect2/', views.redirect2, name='redirect1'),

    # 登陆页面
    path('main/', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('login/showmain/', views.showmain, name='showmain'),
    path('quit/', views.quit, name='quit'),

    # 页面继承
    path('main/', views.main, name='main'),

    # 上传文件
    path('upfile/', views.upfile, name='upfile'),
    path('upfile/savefile/', views.savefile, name='savefile'),

    # 分页
    path('studentpage/<int:pageid>/', views.studentpage, name='pageid'),

    # ajax
    path('ajaxstudents/', views.ajaxstudents, name='ajaxstudents'),
    path('studentsinfo/', views.studentsinfo, name='studentsinfo'),

    # rest练习
    path('rest/', views.rest, name='rest'),
]