#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#      History:
# =============================================================================

import json, time, urllib

from django.core import serializers
from django.shortcuts import render_to_response, get_object_or_404, render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from assets.models import Project, System_usage, Service, Line, ProjectUser, IDC

# 登录
# from accounts.auth_login.auth_index_class import auth_login_required
from django.contrib.auth.decorators import login_required
from cmdb_auth.no_auth import check_auth
from django.http.response import JsonResponse
import requests, re


class product_from(forms.ModelForm):
    class Meta:
        model = Line
        fields = ["name", "slug", "sort"]


@login_required
def product_add(request):
    """
    添加产品线
    """
    init = request.GET.get("init", False)
    status = check_auth(request, "add_line_auth")
    if not status:
        return render(request,'default/error_auth.html', locals())

    content = {}
    server_type = Project.objects.all()

    if request.method == 'POST':
        uf = product_from(request.POST)

        if uf.is_valid():
            zw = uf.save(commit = False)
            zw.save()
            if not init:
                return HttpResponseRedirect('/assets/server/')
            else:
                idc_count = IDC.objects.all().count()
                if idc_count == 0:
                    return HttpResponseRedirect('/assets/idc_add/?init=True')
                else:
                    return HttpResponseRedirect('/assets/host_add/')

    else:
        uf = product_from()
    return render(request,'assets/product_add.html', locals())


@login_required
def product_edit(request, uuid):
    """
    修改产品线
    """
    status = check_auth(request, "add_line_auth")
    if not status:
        return render(request,'default/error_auth.html', locals())
    product_data = Line.objects.get(uuid = uuid)

    if request.method == 'POST':
        uf = product_from(request.POST, instance = product_data)

        if uf.is_valid():
            zw = uf.save()
            return HttpResponseRedirect('/assets/product/list/')

    else:
        uf = product_from(instance = product_data)
    return render(request,'assets/product_add.html', locals())


@login_required
def product_list(request,id=None):
    """
    产品线列表
    """
    if id:
        project_data = Project.objects.filter(line_id=id).values()

        dic=dict()
        dic['list']=list(project_data)


        return JsonResponse(dic)
    status = check_auth(request, "add_line_auth")
    if not status:
        return render(request,'default/error_auth.html', locals())

    product_data = Line.objects.all()
    return render(request,'assets/product_list.html', locals())