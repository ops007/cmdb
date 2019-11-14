from django.conf.urls import include, url
from accounts import views
from django.urls import path,include
urlpatterns = [
    url('^register/',views.userregister,name='register'),
    url('^$',views.index),
    url('^login/',views.userlogin,name='login'),
    url('^logout/',views.userlogout,name='logout'),
]