from django.conf.urls import include, url

from assets.value_class import product_line,business,index
from . import views
from django.urls import path,include
urlpatterns = [
    # 发布申请
    url(r'index/$', views.index),


]