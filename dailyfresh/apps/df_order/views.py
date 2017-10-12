from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.df_cart.models import *
from apps.df_goods.models import *
from apps.df_order.models import *
from apps.df_user.models import *
from ..df_user import user_decorator
from django.db import transaction
from datetime import datetime

# Create your views here.
@user_decorator.login
def order(request,ids):
    username = request.session.get('username')

    id_list = ids.split("_")
    cart_list = CartInfo.objects.filter(goods__in=id_list)
    user = UserInfo.objects.get(uname=username)

    context = {'uname':username,'cart_list':cart_list,"user":user}
    return render(request,"df_order/place_order.html",context)

@transaction.atomic()
def submit(request):
    point = transaction.savepoint()
    username = request.session.get("username","")
    user = UserInfo.objects.get(uname=username)

    post = request.POST
    total = post.get('total')
    addr = post.get('addr')
    now = datetime.now()

    try:
        order = OrderInfo()
        order.oid = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),user.id)
        order.user = user
        order.odate = now
        order.ototal = total
        order.oaddress = addr
        order.save()

        goods = request.POST.get("good_detail")
        goods_list = goods.split(",")

        for good in goods_list:
            good_list = good.split("_")
            odi = OrderDetailInfo()
            odi.goods = GoodsInfo.objects.get(id=good_list[0])
            odi.order = order
            odi.price = good_list[1][0:-1]
            odi.count = good_list[2]
            odi.save()

    except Exception as e:
        print(e)
        transaction.savepoint_rollback(point)
        return HttpResponse("error")

    return redirect('/user/user_center_order/')
