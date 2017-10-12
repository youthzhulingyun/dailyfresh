from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^(\d+)/$', good),
    url(r'^list(\d+)_(\d+)_(\d+)/$', list),
    url(r'^search/', MySearchView()),
]