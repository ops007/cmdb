from django.conf.urls import include, url

from assets.value_class import product_line,business,index
from . import views, service_views
from django.urls import path,include
urlpatterns = [
    # 机房
    url(r'^idc_add/$', views.idc_add),
    url(r'^idc_list/$', views.idc_list),

    # 服务器管理
    url('^host_add/',views.host_add),
    url(r'^host_edit/$', views.host_edit),
    url('^host_list/',views.host_list),
    url(r'^host_add_batch/$', views.host_add_batch),
    url(r'^ip_list/$', views.ip_list),
    url(r'^zabbix/$', views.zabbix_info),
    url(r'^server/type/list/', business.auth_server_type_list),
    url(r'^server/type/add/', business.server_type_add),
    url(r'^server/host_without_business/', index.host_without_business),

    #项目管理
    url(r'^server/$', views.host_list),
    url(r'^server/type/(?P<uuid>[^/]+)/host_list/$', business.business_host_list),
    url(r'^server/type/(?P<uuid>[^/]+)/list/$', business.auth_server_type_list),
    url(r'^server/type/(?P<uuid>[^/]+)/add/$', business.server_type_add),
    url(r'^server/type/edit/(?P<uuid>[^/]+)/$',business.auth_server_type_edit, name="project_edit_ajax"),
    url(r'^server/type/(?P<uuid>[^/]+)/delete/$', business.auth_server_type_user_delete),
    url(r'^server/server_type/$', business.server_type_item),

    # 服务操作
    url(r'service_add/$', service_views.service_add),
    url(r'service_edit/$', service_views.service_edit),
    url(r'service_list/$', service_views.service_list),
    url(r'service_del/$', service_views.service_del),

    # 添加业务线
    url(r'^product/add/$', product_line.product_add),
    url(r'^product/edit/(?P<uuid>[^/]+)/$', product_line.product_edit),
    url(r'product/list/$', product_line.product_list),
    url(r'product/list/(?P<id>[\w]+)$', product_line.product_list),
    url(r'^server/install/$', index.txt_update),
]