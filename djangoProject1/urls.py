"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register),
    path('login/',views.login),
    path('library/',views.library),
    path('books/',views.books),
    path('state/',views.state),
    path('manage/<str:um>/',views.manage),
    path('manage/add/<str:um>/',views.manage_add),
    path("delete/",views.delete),
    path("<int:bid>/edit/<str:um>/",views.edit),
    path("managelogin/",views.manage_login),
    path("teacher_login/",views.teacher_login),
    path("student_login/",views.student_login),
]
