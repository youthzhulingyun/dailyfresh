from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register/$', register),
    url(r'^register_exist/(\w+)/$', register_exist),
    url(r'^register_handle/$', register_handle),
    url(r'^login/$', login),
    url(r'^login_handle/$', login_handle),
    url(r'^exit/$', exit),
    url(r'^user_center_info/$', user_center_info),
    url(r'^user_center_order/$', user_center_order),
    url(r'^user_center_site/$', user_center_site),
    url(r'^site_handle/$', site_handle),
]