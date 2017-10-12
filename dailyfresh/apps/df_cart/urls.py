from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', cart),
    url(r'^add/(\d+)_?(\d*)/$', add),
    # /add/5_3/
    url(r'^edit/(\d+)_(\d+)/$', edit),
    url(r'^dele/(\d+)/$', dele),
]