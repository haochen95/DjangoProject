from django.http import HttpResponse
from .models import Grades,Students
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("school is on time")

def detail(request, num):
    return HttpResponse("details-%s"%(num))

def grades(request):
    # 去数据库中取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板,模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myApp/grades.html', {"grades": gradesList})

def students(request):
    studentList = Students.stuObj.all()
    return render(request, 'myApp/students.html', {"students": studentList})

def gradesStudents(request, number):
    # 获得对应的班级对象
    grades = Grades.objects.get(pk=number)
    # 获得班级下的所有学生列表
    studentsList = grades.students_set.all()
    return render(request, 'myapp/students.html', {"students": studentsList})

def addstudents(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("liudehua",25,True,"I come from china",grade,False)
    stu.save()
    return HttpResponse("Okay, you make it!!")

def attribute(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse('attributes')

# GET
def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + '' + b + '' + c)

def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    b = request.GET.get('b')
    return HttpResponse(a1 + '' + a2 + '' + b)

# POST
def showregist(request):
    return render(request, 'myApp/register.html')

def register(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    hobby = request.POST.getlist('hobby')
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse('post')

# RESPONSE

def showresponse(request):
    res = HttpResponse()
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res

def cookietest(request):
    res = HttpResponse()
    # 存cookie
    # cookie = res.set_cookie('suck', 'good')
    # 用cookie
    cok = request.COOKIES
    res.write('<h1>' + cok['suck'] + '</h1>')
    # 删除cookie
    return res


# 重定向
from django.http import HttpResponseRedirect

def redirect1(request):
    return HttpResponseRedirect('/redirect2/')

def redirect2(request):
    return HttpResponse("我是重定向后的视图")


# 欢迎-登陆界面

def main(request):
    # 取session
    username = request.session.get('name', '游客')
    return render(request, 'myApp/main.html', {'username':username})


def login(request):
    return render(request, 'myApp/login.html')


def showmain(request):
    username = request.POST.get('username')
    # 存session
    request.session['name'] = username
    return redirect('/main')

from django.contrib.auth import logout
def quit(request):
    # 清除session
    logout(request)
    return redirect('/main')



# 页面继承

def main(request):
    return render(request, 'myApp/page01.html')

# 上传页面

def upfile(request):
    return render(request, 'myApp/upfile.html')

import os
from django.conf import settings

def savefile(request):
    if request.method == "POST":
        f = request.FILES["file"]
        # 文件在服务端的路径
        filepath = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(filepath, 'wb') as fp:
            for info in f.chunks():
                fp.write(info)
        return HttpResponse("上传成功")
    else:
        return HttpResponse("上传失败")

from django.core.paginator import Paginator

def studentpage(request, pageid):
    # 所有学生列表
    allList = Students.stuObj.all()

    paginator = Paginator(allList, 5)
    page = paginator.page(pageid)
    print(page)

    return render(request, 'myApp/studentpage.html', {'students': page})


def ajaxstudents(request):
    return render(request, 'myApp/ajaxStudents.html')

from django.http import JsonResponse

def studentsinfo(request):
    stu = Students.stuObj.all()

    list = []
    for s in stu:
        list.append([s.sname, s.sage])

    return JsonResponse({"data":list })


def rest(request):

    pass
