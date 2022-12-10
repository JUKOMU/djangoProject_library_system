from django.shortcuts import render,HttpResponse,redirect
from django.db.models import Q
from app1 import models
import os
import shutil
from django.template import RequestContext
# Create your views here.

"""
通过关键字s获取post请求发来的数据
"""
def get(request,s):
    return request.POST.get(s)


"""
处理发送到/register/的请求
"""
def register(request):
    if request.method == "GET":
        #get请求直接返回页面
        return render(request,"register.html")
    if request.method == "POST":
        # 获取post请求数据
        u=get(request,'username')
        p1=get(request,'password')
        p2=get(request,'newpassword')
        #判断post请求数据
        if u=="":
            return render(request,"register.html", {"n1":"用户名不能为空!"})
        elif p1=="":
            return render(request,"register.html", {"n1":"密码不能为空!"})
        elif p2=="":
            return render(request,"register.html", {"n1":"确认密码不能为空!"})
        elif p1 != p2:
            return render(request, "register.html", {"n1": "两次输入的密码不同!"})
        else:
            # 查询数据库
            data_list = models.UserInf.objects.all()
            for obj in data_list:
                if u == obj.name:
                    return render(request,"register.html", {"n1":"该用户名已被注册!"})
            """
            无查询结果，注册该用户，并返回提示登录信息
            """
            models.UserInf.objects.create(name=u,password=p1)
            return render(request, "register.html", {"n1": "注册成功!","n2": "点击登录"})


"""
处理发送到/login/的请求
"""
def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    if request.method == "POST":
        # 比较post数据和数据库中数据
        u = get(request, 'username')
        p = get(request, 'password')
        data_list=models.UserInf.objects.all()
        for obj in data_list:
            if u == obj.name:
                if p == obj.password:
                    return render(request,"library.html",{"user":u})
                else:
                    return render(request,"login.html",{"n":"密码错误!"})
        return render(request,"login.html",{"n":"该用户不存在!"})


"""
返回图书主界面
"""
def library(request):
    if request.method == "GET":
        return render(request,"library.html")
    if request.method == "POST":
        return HttpResponse("不支持的操作!")


"""
图书查询
"""
def books(request):
    if request.method == "GET":
        return HttpResponse("请登录!")
    if request.method == "POST":
        # 判断是否为未登录用户
        u=get(request,'name')
        if u != "AnonymousUser":
            #用户已登陆，返回查询结果
            k=get(request,'keyword')
            # 获取查询关键字
            if k != None and k !="":
                if k == "all":
                    book_list = models.BooksInf.objects.all()
                    return render(request, "books.html", {"book": book_list})
                else:
                    book_list=models.BooksInf.objects.filter(Q(bauthor__contains=k)|Q(bname__contains=k))
                    return render(request,"books.html",{"book":book_list})
            else:
                return render(request,"books.html")
        # 用户未登录，返回提示登录信息
        else:
            return HttpResponse("请登录!")


"""
状态查询
"""
def state(request):
    if request.method == "GET":
        return HttpResponse("请登录!")
    if request.method == "POST":
        # 判断是否为未登录用户
        u=get(request,'name')
        if u != "AnonymousUser":
            # 用户已登陆，返回查询结果
            k=get(request,'keyword')
            # 获取状态查询关键字
            if k != None and k !="":
                if k == "all":
                    book_list = models.BooksInf.objects.all()
                    return render(request, "books.html", {"book": book_list})
                else:
                    book_list=models.BooksInf.objects.filter(bstate=k)
                    return render(request,"state.html",{"book":book_list})
            else:
                return render(request,"state.html")
        # 用户未登录，返回提示登录信息
        else:
            return HttpResponse("请登录!")


"""
管理员页面，通过manage_login(request)传递管理员名字“um”
"""
def manage(request,um):
        book_list = models.BooksInf.objects.all()
        return render(request,"manage.html",{"book":book_list,"n":um})


"""
实现添加书的功能
"""
def manage_add(request,um):
    # 判断是否为管理员
    if um == "admin":
        #获取新增图书信息
        b=get(request,"bname")
        i=get(request,"bimg")
        a=get(request,"bauthor")
        s=get(request,"bstate")
        # 查询是否图书重名
        blist=models.BooksInf.objects.filter(bname=b)
        if blist.count()==0:
            # 当信息不重复且不为空时添加图书信息
            if b != "" and a !="" and i!="" and s!="":
                # 将封面图片拷贝至bimg文件夹中vvvvvv
                i=str(i)
                file_type=os.path.splitext(i)[-1]
                file_type=file_type.replace('"','')
                shutil.copy(i,r"E:\djangoProject1\app1\static\img\bimg\\"+b+file_type)
                # 将封面图片拷贝至bimg文件夹中^^^^^^
                i=b+file_type
                # 添加图书信息
                models.BooksInf.objects.create(bname=b, bauthor=a,bimg=i,bstate=s,)
                return redirect("/manage/"+um)
        return redirect("/manage/"+um)
    return render(request,"managelogin.html")


""""
删除操作，不可撤销!
"""
def delete(request):
    models.BooksInf.objects.filter(id=request.GET.get('bid')).delete()
    return redirect("/manage/")


"""
编辑操作
"""
def edit(request,bid,um):
    if request.method == "GET":
        # 显示要编辑的图书信息
        book = models.BooksInf.objects.filter(id=bid)
        return render(request, "edit.html", {"book": book,"n":um})
    if request.method == "POST":
        # 获取更新后图书信息
        b = get(request, "bname")
        i = get(request, "bimg")
        a = get(request, "bauthor")
        s = get(request, "bstate")
        if b != "" and a != "" and i != "" and s != "":
            o=models.BooksInf.objects.filter(id=bid).first()
            # 图书封面文件更新
            if i != o.bimg:
                i = str(i)
                file_type = os.path.splitext(i)[-1]
                file_type = file_type.replace('"', '')
                # 删除原封面
                os.remove(os.path.join(r"E:\djangoProject1\app1\static\img\bimg",str(o.bimg)))
                # 复制新封面
                shutil.copy(i, r"E:\djangoProject1\app1\static\img\bimg\\" + b + file_type)
                i = b + file_type
            # 更新图书信息
            models.BooksInf.objects.filter(id=bid).update(bname=b, bauthor=a, bimg=i, bstate=s, )
            return redirect("/manage/"+um)
        return redirect("/manage/"+um)


"""
管理员登录
"""
def manage_login(request):
    if request.method == "GET":
        return render(request,"managelogin.html")
    if request.method == "POST":
        u = get(request, 'username')
        p = get(request, 'password')
        if u == "admin" and p == "123":
            # 判断是否为管理员
            url1="/manage/"+u+"/"
            return redirect(url1)
        return render(request,"managelogin.html")

def teacher_login(request):
    if request.method == "GET":
        return render(request,"teacher_login.html")
    if request.method == "POST":
        # 比较post数据和数据库中数据
        u = get(request, 'username')
        p = get(request, 'password')
        data_list = models.UserInf.objects.all()
        for obj in data_list:
            if u == obj.name:
                if p == obj.password:
                    return render(request, "library.html", {"user": u})
                else:
                    return render(request, "login.html", {"n": "密码错误!"})
        return render(request, "login.html", {"n": "该用户不存在!"})


def student_login(request):
    if request.method == "GET":
        return render(request,"student_login.html")
    if request.method == "POST":
        # 比较post数据和数据库中数据
        u = get(request, 'username')
        p = get(request, 'password')
        data_list = models.UserInf.objects.all()
        for obj in data_list:
            if u == obj.name:
                if p == obj.password:
                    return render(request, "library.html", {"user": u})
                else:
                    return render(request, "login.html", {"n": "密码错误!"})
        return render(request, "login.html", {"n": "该用户不存在!"})

