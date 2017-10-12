from hashlib import sha1

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect

from apps.df_order.models import *
from . import user_decorator
from .models import *
from ..df_goods.models import GoodsInfo


def register(request):
    return render(request, 'df_user/register.html')


def register_exist(request, uname):
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({"data": count})


def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    uemail = post.get('email')

    s1 = sha1()
    s1.update(upwd.encode())
    upwd_sha1 = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.uemail = uemail
    user.save()

    return render(request, 'df_user/login.html')


def login(request):
    context = {"error": request.session.get('error', ""), "username": request.COOKIES.get("username", "")}
    return render(request, 'df_user/login.html', context)


def login_handle(request):
    username = request.POST['username']
    pwd = request.POST['pwd']
    jizhu = request.POST.get("jizhu", '0')

    s1 = sha1()
    s1.update(pwd.encode())
    pwd_sha1 = s1.hexdigest()

    info = UserInfo.objects.filter(uname=username)

    if len(info) == 0:
        request.session['error'] = "username"
        return redirect("/user/login/")
    else:
        pwd_db = info[0].upwd
        if pwd_db == pwd_sha1:
            request.session['error'] = ""
            request.session['username'] = username
            url = request.COOKIES.get('url', '/user_center_info/')
            red = HttpResponseRedirect(url)
            if jizhu == "1":
                red.set_cookie('username', username)
            return red
        else:
            request.session['error'] = "password"
            return redirect("/user/login/")


def exit(request):
    del request.session['username']
    # count = python_count
    # del request.session[count]
    return redirect("/")


@user_decorator.login
def user_center_info(request):
    username = request.session.get("username")

    good_ids = request.COOKIES.get(username, "")
    if good_ids == "":
        good_id_list = []
    elif "," in good_ids:
        good_id_list = good_ids.split(",")
    else:
        good_id_list = [good_ids]

    good_list = []
    for i in good_id_list:
        good = GoodsInfo.objects.get(id=i)
        good_list.append(good)

    info = UserInfo.objects.filter(uname=username)

    uname = info[0].uname
    uphone = info[0].uphone
    uaddress = info[0].uaddress

    context = {"uname": uname, "uphone": uphone, "uaddress": uaddress,'good_list':good_list}

    return render(request, "df_user/user_center_info.html", context)


@user_decorator.login
def user_center_order(request):
    username = request.session.get("username")
    orders = OrderInfo.objects.all()
    dict = request.GET
    index = dict.get("index",1)

    pagintor = Paginator(orders,1)
    index = int(index)

    orders = pagintor.page(index)

    # plist = pagintor.page_range
    page = pagintor.page(index)

    context = {"uname": username,"orders":orders,"page":page}
    return render(request, "df_user/user_center_order.html", context)


@user_decorator.login
def user_center_site(request):
    username = request.session.get("username")
    info = UserInfo.objects.get(uname=username)

    context = {"uname":username,"user":info}

    return render(request, "df_user/user_center_site.html", context)


def site_handle(request):
    username = request.session.get("username")
    info = UserInfo.objects.filter(uname=username)
    dict = request.GET
    info.update(uaddress=dict.get("site_area"))
    info.update(uphone=dict.get("uphone"))
    info.update(upostcode=dict.get("upostcode"))
    return redirect("/user/user_center_site/")
