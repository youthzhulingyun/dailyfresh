from django.core.paginator import Paginator
from django.shortcuts import render

from apps.df_cart.models import CartInfo
from apps.df_user.models import UserInfo
from .models import *
from haystack.views import SearchView

# Create your views here.
def index(request):
    username = request.session.get("username","")
    type_list = TypeInfo.objects.all()
    type0 = type_list[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = type_list[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = type_list[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = type_list[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = type_list[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = type_list[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = type_list[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = type_list[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = type_list[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = type_list[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = type_list[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = type_list[5].goodsinfo_set.order_by('-gclick')[0:4]

    if username != "":
        user = UserInfo.objects.get(uname=username)
        cart_count = CartInfo.objects.filter(user=user).count()
    else:
        cart_count = 0

    context={'uname':username,'type0':type0,'type01':type01,'type1':type1,'type11':type11,'type2':type2,'type21':type21,'type3':type3,'type31':type31,'type4':type4,'type41':type41,'type5':type5,'type51':type51,"cart_count":cart_count}
    return render(request,"df_goods/index.html",context)

def good(request,id):
    username = request.session.get("username","")
    good = GoodsInfo.objects.get(id=id)
    good.gclick+=1
    good.save()
    goods_new = GoodsInfo.objects.order_by('-id')[0:2]

    if username != "":
        user = UserInfo.objects.get(uname=username)
        cart_count = CartInfo.objects.filter(user=user).count()
    else:
        cart_count = 0

    context = {'uname':username,'good':good,'goods_new':goods_new,"cart_count":cart_count}
    response = render(request,'df_goods/detail.html',context)

    if username != '' and username != None:
        good_ids = request.COOKIES.get(username,"")
        if good_ids == "":
            good_id_list = []
        elif "," in good_ids:
            good_id_list = good_ids.split(",")
        else:
            good_id_list = [good_ids]

        if len(good_id_list) >= 5:
            good_id_list.pop(0)

        for i in good_id_list:
            if i == id:
                break
        else:
            good_id_list.append(id)

        good_ids = ""
        for temp in  good_id_list:
            good_ids += (temp + ",")

        good_ids = good_ids[0:-1]
        response.set_cookie(username,good_ids)

    return response

def list(request,n,o,p):
    type = TypeInfo.objects.get(id=n)

    if o == "1":
        goods = type.goodsinfo_set.order_by('-id')
    elif o == "2":
        goods = type.goodsinfo_set.order_by('gprice')
    elif o == "3":
        goods = type.goodsinfo_set.order_by('-gclick')

    paginator = Paginator(goods, 2)
    p = int(p)
    goods = paginator.page(p)
    # 获取所有的页码信息
    plist = paginator.page_range

    goods_new = GoodsInfo.objects.order_by('-id')[0:2]
    username = request.session.get("username","")

    if username != "":
        user = UserInfo.objects.get(uname=username)
        cart_count = CartInfo.objects.filter(user=user).count()
    else:
        cart_count = 0

    context = {'uname': username,'n':n,'o':o,'p':p,'goods':goods,'plist':plist,'goods_new':goods_new,'cart_count':cart_count}
    return render(request, 'df_goods/list.html', context)


class MySearchView(SearchView):
    def extra_context(self):
        context = super().extra_context()
        username = self.request.session.get('username')
        user = UserInfo.objects.get(uname=username)
        cart_count = CartInfo.objects.filter(user=user).count()
        context['uname'] = username
        context['cart_count'] = cart_count
        return context


