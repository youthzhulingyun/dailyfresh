from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from apps.df_goods.models import GoodsInfo
from apps.df_user.models import UserInfo
from .models import *
from ..df_user import user_decorator


# Create your views here.
@user_decorator.login
def cart(request):
    username = request.session.get('username')
    user = UserInfo.objects.get(uname=username)
    cart_list = CartInfo.objects.filter(user=user)
    count = cart_list.count()
    context = {"uname": username, 'cart_list': cart_list, 'count': count}
    return render(request, 'df_cart/cart.html', context)


@user_decorator.login
def add(request, good_id,good_count):

    if good_count == "":
        good_count = 1

    username = request.session.get('username', "")
    user = UserInfo.objects.get(uname=username)

    if CartInfo.objects.filter(goods_id=good_id).count() > 0:
        cart = CartInfo.objects.get(goods_id=good_id)
        cart.count += int(good_count)
        cart.save()
    else:
        cart = CartInfo()
        cart.user = user
        cart.goods_id = good_id
        cart.count = 1
        cart.save()

    if request.is_ajax():
        count = CartInfo.objects.filter(user=user).count()
        return JsonResponse({'count': count})


def edit(request,id,count):
    username = request.session.get('username')
    uid = UserInfo.objects.get(uname=username)
    cart = CartInfo.objects.get(user_id=uid,goods_id=id)
    cart.count = count
    cart.save()
    return JsonResponse({})


def dele(request,good_id):
    username = request.session.get('username')
    uid = UserInfo.objects.get(uname=username)
    cart = CartInfo.objects.get(user_id=uid, goods_id=good_id)
    cart.delete()
    return redirect("/cart/")

