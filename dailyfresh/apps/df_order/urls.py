from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^submit/$',submit),
    url(r'^(\w+)/$',order),
]