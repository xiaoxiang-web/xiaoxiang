from django.shortcuts import render, HttpResponse, redirect, Http404
from django.urls import reverse,resolve

from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from django.core.paginator import Paginator
# Create your views here.
def Login(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('passward')
        print(a, b)
        if request.POST.get('username'):
            if User.objects.filter(username=a):
                # print(request.GET.get('next'))
                f = authenticate(username=a, password=b)
                if f:
                    login(request, user=f)
                    return redirect(reverse('teacher_list'),locals())

                errors = '密码错误'
            else:
                errors = '用户名错误'

        else:
            errors = '用户名为空'
        return render(request, 'login.html', locals())
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        # b = make_password(request.POST.get('passward'))
        b=request.POST.get('passward')
        if request.POST.get('username'):
            if User.objects.filter(username=a):
                return HttpResponse('用户已存在')
            else:
                # user.objects.create(username=a, password=b)

                User.objects.create_user(username=a,password=b)#create_user创建保存一个is_active为True的USER对象,并且自动为密码加密，不需要我们自己加密
                i = authenticate(username=a, password=b)
                if i:
                    print(2)
                    login(request, user=i)
                    username = request.user
                    return redirect(reverse('manages'))
                return HttpResponse('注册成功')
        else:
            errors = '用户名不能为空'
            return render(request, 'register.html', locals())
    return render(request, 'register.html')
def outlogin(request):
    logout(request)
    return redirect(reverse('login'))
@login_required(login_url='/login/')
def manages(request):
    return render(request,'manages.html')
@login_required(login_url='/login/')
def teacher_list(request):
    tea=teachers.objects.all().order_by('id')
    username = request.user
    return render(request,'manages.html',locals())
def class_list(request):
    cla=classes.objects.all().order_by('id')
    username = request.user
    return render(request,'class_list.html',locals())
def course_list(request):
    course=lessons.objects.all().order_by('Class_id')
    username = request.user
    return render(request,'course_list.html',locals())
def teacher_add(request):
    if request.method=='POST':
        a=request.POST.get('name')
        if teachers.objects.filter(name=a):
            errors='该教师已存在'
            return render(request,'teacher_add.html',locals())
        b=request.POST.get('subject')
        if not a or not b:
            errors='输入为空'
            return render(request, 'teacher_add.html', locals())
        teachers.objects.create(name=a,subject=b)
        return redirect(reverse('teacher_list'))
    username = request.user
    return render(request,'teacher_add.html')
def teacher_edit(request):
    id=request.GET.get('id')
    tea=teachers.objects.get(id=id)
    username = request.user
    if request.method=="POST":
        id=request.GET.get('id')
        tea=teachers.objects.get(id=id)
        a=request.POST.get('name')
        b=request.POST.get('subject')
        if not a or not b:
            errors='输入为空'
            return render(request, 'teacher_edit.html', locals())
        if teachers.objects.filter(name=a):
            errors="该教师已存在"
            return render(request,'teacher_edit.html',locals())
        print(a)
        print(b)
        tea.name=a
        tea.subject=b
        tea.save()
        return redirect(reverse('teacher_list'))
    return render(request,'teacher_edit.html',locals())
def teacher_del(request):
    id=request.GET.get('id')
    teachers.objects.filter(id=id).delete()
    return redirect(reverse('teacher_list'))
def class_add(request):
    if request.method=='POST':
        a=request.POST.get('name')
        if classes.objects.filter(name=a):
            errors='该班级已存在'
            return render(request,'class_add.html',locals())
        b=request.POST.get('quantity')
        if not a or not b:
            errors='输入为空'
            return render(request, 'class_add.html', locals())
        classes.objects.create(name=a,student_quantity=b)
        return redirect(reverse('class_list'))
    username = request.user
    return render(request,'class_add.html')
def class_edit(request):
    id=request.GET.get('id')
    cla=classes.objects.get(id=id)
    if request.method=='POST':
        a=request.POST.get('name')
        b=request.POST.get('quantity')
        if not a or not b:
            errors='输入为空'
            return render(request, 'class_edit.html', locals())
        if classes.objects.filter(name=a):
            errors = '该班级已存在'
            return render(request, 'class_edit.html', locals())
        cla.name=a
        cla.student_quantity=b
        cla.save()
        return redirect((reverse('class_list')))
    username = request.user
    return render(request,'class_edit.html',locals())
def class_del(request):
    id=request.GET.get('id')
    classes.objects.filter(id=id).delete()
    return redirect(reverse('class_list'))
def course_add(request):
    teacher=teachers.objects.all().order_by('id')
    Class=classes.objects.all().order_by('id')
    weeks=["周一","周二","周三","周四","周五",]
    sections=['第1节','第2节','第3节','第4节','第5节','第6节','第7节','第8节']
    if request.method=='POST':
        b=request.POST.get('teacher')
        c=request.POST.get('class')
        d=request.POST.get('week')
        e=request.POST.get('section')
        if lessons.objects.filter(teacher=b,Class=c,week=d,section=e):
            errors='该课程已被添加'
            return render(request,'course_add.html',locals())
        elif lessons.objects.filter(teacher=b,week=d,section=e):
            errors='该老师这时间段已有课程安排'
            return render(request,'course_add.html',locals())
        elif lessons.objects.filter(Class=c,week=d,section=e):
            errors = '该班级这时间段已有课程安排'
            return render(request, 'course_add.html', locals())
        lessons.objects.create(Class_id=c,teacher_id=b,week=d,section=e)
        return redirect(reverse('course_list'))
    username = request.user
    return render(request,'course_add.html',locals())
def course_edit(request):
    teacher=teachers.objects.all().order_by('id')
    Class=classes.objects.all().order_by('id')
    weeks=["周一","周二","周三","周四","周五",]
    sections=['第1节','第2节','第3节','第4节','第5节','第6节','第7节','第8节']
    if request.method=="POST":
        id=request.GET.get('id')
        lesson=lessons.objects.get(id=id)
        b=request.POST.get('teacher')
        c=request.POST.get('class')
        d=request.POST.get('week')
        e=request.POST.get('section')
        if lessons.objects.filter(teacher=b,Class=c,week=d,section=e):
            errors='该课程已被添加'
            return render(request,'course_add.html',locals())
        elif lessons.objects.filter(teacher=b,week=d,section=e):
            errors='该老师这时间段已有课程安排'
            return render(request,'course_add.html',locals())
        elif lessons.objects.filter(Class=c,week=d,section=e):
            errors = '该班级这时间段已有课程安排'
            return render(request, 'course_add.html', locals())
        lesson.teacher_id = b
        lesson.Class_id = c
        lesson.week = d
        lesson.section = e
        lesson.save()
        return redirect(reverse('course_list'))
    username = request.user
    return render(request,'course_edit.html',locals())
def course_del(request):
    id=request.GET.get('id')
    lessons.objects.filter(id=id).delete()
    return redirect(reverse('course_list'))
def schedule(request):
    id=None
    if request.method=="POST":
        id=request.POST.get('class')
    Class=classes.objects.all().order_by('id')
    if not id:
        cla=classes.objects.first()
    else:
        cla=classes.objects.get(id=id)
    courses=[[[' ',' '] for j in range(5)] for i in range(8)]
    for i in range(1,9):
        for j in range(1,6):
            if lessons.objects.filter(Class__name=cla.name,week=j,section=i):
                f=lessons.objects.get(Class__name=cla.name,week=j,section=i)
                courses[i-1][j-1]=[f.teacher.name,f.teacher.subject]
    username=request.user
    return render(request,'schedule.html',locals())
