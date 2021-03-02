"""web1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login),
    path('login/',Login,name='login'),
    path('logout/',outlogin,name='logout'),
    path('register/',register,name='register'),
    path('manages/',manages,name='manages'),
    path('teacher_list/',teacher_list,name='teacher_list'),
    path('class_list/',class_list,name='class_list'),
    path('course_list/',course_list,name='course_list'),
    path('teacher_add/',teacher_add,name='teacher_add'),
    path('teacher_del/',teacher_del,name='teacher_del'),
    path('teacher_edit/',teacher_edit,name='teacher_edit'),
    path('class_add/', class_add, name='class_add'),
    path('class_del/', class_del, name='class_del'),
    path('class_edit/',class_edit,name='class_edit'),
    path('course_add/', course_add, name='course_add'),
    path('course_del/', course_del, name='course_del'),
    path('course_edit/',course_edit,name='course_edit'),
    path('schedule/',schedule,name='schedule'),

]
