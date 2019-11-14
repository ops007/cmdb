from django.shortcuts import render_to_response, get_object_or_404, render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect

from assets.forms import business_form
from assets.zabbix import zabbix_group_add
from cmdb_auth.no_auth import check_auth
from mysite.config import zabbix_on
from users.models import CustomUser

from assets.models import Host, IDC, Server_System, Cores, System_os, system_arch
from assets.models import Project, System_usage, Service, Line, ProjectUser
# from accounts.auth_login.auth_index_class import auth_login_required
from django.contrib.auth.decorators import login_required
from assets.models import ENVIRONMENT
from users.models import server_auth, department_Mode
from assets.models import project_swan


import time
import ast


@login_required()
def business_host_list(request, uuid):
    """
    项目主机列表
    """
    context = {}
    item = get_object_or_404(Project, uuid=uuid)
    # 此处权限还需在验证，直接返回 404对异步操作体验很不友好
    # //t = get_object_or_404(ProjectUser, myform=item, user=request.user)   # check permissions
    business_item = Project.objects.get(uuid=uuid)
    form_user = ProjectUser.objects.filter(project=business_item)

    form_user = [one.user for one in form_user]
    user = CustomUser.objects.get(pk=request.user.id)

    if request.user not in form_user:
        return render(request, 'ansible/server_type_node_error.html', locals())

    all_env = ENVIRONMENT
    env = request.GET.get("env", None)
    form_user_auth = ProjectUser.objects.get(project=business_item, user=user)
    user_env = ast.literal_eval(form_user_auth.env)

    if env:
        if env == "all":
            host_list = business_item.host_set.all()
        else:
            host_list = business_item.host_set.filter(env=env)
        return render(request,'assets/host_list_widget.html', locals())
    return render(request, 'ansible/server_type_node.html', locals())



# 业务管理
@login_required
def auth_server_type_list(request):
    # status = check_auth(request, "project_auth")
    # if not status:
    #     return render_to_response('default/error_auth.html', locals(), context_instance=RequestContext(request))

    business_list = Project.objects.all()

    swan_all = project_swan.objects.all()
    return render(request,'assets/server_type_list.html', locals())


# 业务管理
@login_required
@csrf_protect
def server_type_add(request):
    """
    添加项目方法，用于主机业目分配
    """
    status = check_auth(request, "add_project")
    if not status:
        return render(request,'default/error_auth.html', locals())

    if request.method == 'POST':  # 验证post方法
        uf = business_form(request.POST)  # 绑定POST动作
        init = request.GET.get("init", False)
        if uf.is_valid():
            uf.save()
            project_name = uf.cleaned_data['service_name']
            if zabbix_on:
                ret = zabbix_group_add(project_name)
                if ret == 0:
                    pass
            if not init:
                return HttpResponseRedirect("/assets/server/type/list/")
            else:
                return HttpResponseRedirect("/assets/host_add/")
    else:
        uf = business_form()
        try:
            dev_group = department_Mode.objects.get(desc_gid=1003)
            user_list = CustomUser.objects.filter(department_id=dev_group.id)
        except:
            pass
        user_group = []
        # user_list = CustomUser.objects.filter(is_superuser__isnull=True)
    return render(request,'assets/server_type_add.html', locals())



@login_required
@csrf_protect
def auth_server_type_edit(request, uuid):
    """
    业务修改模块
    """
    status = check_auth(request, "edit_project")
    if not status:
        return render(request,'auth/auth_jquery.html', locals())

    server_type = Project.objects.all()
    business_name = Project.objects.get(uuid=uuid)
    form_user_qs = ProjectUser.objects.filter(project=business_name)
    form_user = [one.user for one in form_user_qs]
    uf = business_form(instance=business_name)

    try:
        dev_group = department_Mode.objects.get(desc_gid=1003)
        dev_group_userlist = CustomUser.objects.filter(department_id=dev_group.id)
    except:
        pass

    if business_name.project_user_group:
        user_list_id = [int(i) for i in ast.literal_eval(business_name.project_user_group)]

    if request.method == 'POST':
        uf = business_form(request.POST, instance=business_name)
        if uf.is_valid():
            myform = uf.save()
            return render(request,'assets/server_type_edit_ok.html', locals())

    return render(request,'assets/server_type_edit.html', locals())



@login_required
@csrf_protect
def auth_server_type_user_delete(request, id):
    """
    delete Project's user
    """
    user_id = request.GET.get("user_id", '-1')
    user = get_object_or_404(CustomUser, pk=user_id)
    business_item = Project.objects.get(id=id)
    form_user = ProjectUser.objects.filter(user=user, myform=business_item)
    form_user.delete()

    user_all = CustomUser.objects.all()
    form_user = ProjectUser.objects.filter(myform=business_item)
    form_one_user = [one.user for one in form_user]
    user_test = [one.env for one in form_user]
    rest_user = [one for one in user_all if one not in form_one_user and not one.is_superuser]

    return render(request,'assets/server_type_user_edit.html', locals())



@login_required
@csrf_protect
def server_type_item(request):
    service_name = request.GET.get("service_name")
    business_name = Project.objects.get(service_name=service_name)
    server_list = business_name.host_set.all()
    server_list_count = server_list.count()

    centos = business_name.host_set.filter(system="CentOS").count()

    business_list = []
    for i in server_list:
        business_list.append({i.eth1: i.business.all()})

    return render(request,'assets/host_list.html', locals())
