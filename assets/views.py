from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from accounts.new_api import pages
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def host_add(request):
    """ 添加主机 """
    uf = HostForm()
    projects = Project.objects.all()
    services = Service.objects.all()

    if request.method == 'POST':
        uf_post = HostForm(request.POST)
        physics = request.POST.get('physics', '')
        ip = request.POST.get('eth1', '')
        if Host.objects.filter(eth1=ip):
            emg = u'添加失败, 该IP %s 已存在!' % ip
            return render(request, 'assets/host_add.html', locals())
        if uf_post.is_valid():
            zw = uf_post.save(commit=False)
            zw.mac = str(request.POST.getlist("mac")[0]).replace(':', '-').strip(" ")
            status = uf_post.cleaned_data['status']
            if physics:
                physics_host = get_object_or_404(Host, eth1=physics)
                zw.vm = physics_host
                zw.type = 1
            else:
                zw.type = 0
            zw.save()
            uf_post.save_m2m()
            # if zabbix_on and status == 1:
            #     zabbix_host_add(request)
            smg = u'主机%s添加成功!' % ip
            return render(request,'assets/host_add.html', locals())

    # return render(request, 'assets/host_add.html', locals())
    return render(request,'assets/host_add.html', locals())

@login_required
def idc_add(request):
    """ 添加IDC """
    if request.method == 'POST':
        init = request.GET.get("init", False)

        uf = IdcForm(request.POST)
        if uf.is_valid():
            idc_name = uf.cleaned_data['name']
            if IDC.objects.filter(name=idc_name):
                emg = u'添加失败, 此IDC %s 已存在!' % idc_name
                return render(request,'assets/idc_add.html', locals())
            uf.save()
            # if zabbix_on:
            #     ret = zabbix_group_add(idc_name)
            #     if ret != 1:
            #         emg = u'添加zabbix主机组 %s 失败!' % idc_name
            #         return render(request,'assets/idc_add.html', locals())
            if not init:
                return HttpResponseRedirect("/assets/idc_list/")
            else:
                return HttpResponseRedirect('/assets/server/type/add/?init=true')

    else:
        uf = IdcForm()
    return render(request,'assets/idc_add.html', locals())

@login_required
def idc_list(request):
    idcs = IDC.objects.all()
    server_type = Project.objects.all()
    return render(request,'assets/idc_list.html', locals())

@login_required
def host_list(request):
    """ 主机列表 """
    hosts = Host.objects.all().order_by("-eth1")
    idcs = IDC.objects.filter()
    lines = Line.objects.all()
    server_type = Project.objects.all()
    services = Service.objects.all()
    brands = Server_System
    server_status = SERVER_STATUS
    server_list_count = hosts.count()
    physics = Host.objects.filter(vm__isnull=True).count()
    vms = Host.objects.filter(vm__isnull=False).count()
    contact_list, p, contacts, page_range, current_page, show_first, show_end = pages(hosts, request)

    return render(request,'assets/host_list.html', locals())

@login_required
@csrf_protect
def host_add_batch(request):
    """ 批量添加主机 """
    if request.method == 'POST':
        multi_hosts = request.POST.get('batch').split('\n')
        for host in multi_hosts:
            if host == '':
                break
            print(host)
            print(len(host.split("@")))
            print(host.split("@"))
            node_name, cpu, memory, hard_disk, number, brand,  eth1, eth2, internal_ip, idc, comment,  = host.split('@')
            print(idc)
            asset = Host(node_name=node_name, number=number, brand=brand,  cpu=cpu,
                         memory=memory, hard_disk=hard_disk, eth1=eth1,
                         eth2=eth2, internal_ip=internal_ip, editor=comment)
            asset.save()
        smg = u'批量添加成功.'
        return render(request,'assets/host_add_batch.html', locals())

    return render(request, 'assets/host_add_batch.html', locals())

@login_required
def ip_list(request):
    """ ip列表 """
    idcs = IDC.objects.all()
    # yizhuang_idc = get_object_or_404(IDC, name='亦庄电信')
    # active_111 = IpList.objects.filter(idc=yizhuang_idc, network='192.168.111.0/24', status=1)
    # unactive_111 = IpList.objects.filter(idc=yizhuang_idc, network='192.168.111.0/24', status=1)
    # active_112 = IpList.objects.filter(idc=yizhuang_idc, network='192.168.112.0/24', status=1)
    # unactive_112 = IpList.objects.filter(idc=yizhuang_idc, network='192.168.112.0/24', status=1)
    # active_113 = IpList.objects.filter(idc=yizhuang_idc, network='192.168.113.0/24', status=1)
    # unactive_113 = IpList.objects.filter(idc=yizhuang_idc, network='192.168.113.0/24', status=1)
    return  render(request,'assets/ip_list.html', locals())

@login_required
def zabbix_info(request):
    """ zabbix信息 """
    records = ZabbixRecord.objects.all()
    return render(request,'assets/zabbix.html', locals())


def db_to_record(username, host, info):
    text_list = []
    for k, v in info.items():
        field = Host._meta.get_field_by_name(k)[0].verbose_name
        if k == 'idc':
            old = IDC.objects.filter(uuid=v[0])
            new = IDC.objects.filter(uuid=v[1])
            if old:
                name_old = old[0].name
            else:
                name_old = u'无'
            if new:
                name_new = new[0].name
            else:
                name_new = u'无'
            text = field + u'由 ' + name_old + u' 更改为 ' + name_new

        elif k == 'service':
            old, new = [], []
            for s in v[0]:
                service_name = Service.objects.get(uuid=s).name
                old.append(service_name)
            for s in v[1]:
                service_name = Service.objects.get(uuid=s).name
                new.append(service_name)
            text = field + u'由 ' + ','.join(old) + u' 更改为 ' + ','.join(new)

        elif k == 'business':
            old, new = [], []
            for s in v[0]:
                project_name = Project.objects.get(uuid=s).service_name
                old.append(project_name)
            for s in v[1]:
                project_name = Project.objects.get(uuid=s).service_name
                new.append(project_name)
            text = field + u'由 ' + ','.join(old) + u' 更改为 ' + ','.join(new)

        elif k == 'vm':
            old = Host.objects.filter(uuid=v[0])
            new = Host.objects.filter(uuid=v[1])
            if old:
                name_old = old[0].eth1
            else:
                name_old = u'无'
            if new:
                name_new = new[0].eth1
            else:
                name_new = u'无'
            text = field + u'父主机由 ' + name_old + u' 更改为 ' + name_new

        else:
            text = field + u'由 ' + str(v[0]) + u' 更改为 ' + str(v[1])
        text_list.append(text)

    if len(text_list) != 0:
        HostRecord.objects.create(host=host, user=username, content=text_list)


def get_diff(obj1, obj2):
    fields = ['service', 'business']
    no_check_fields = ['cpu', 'core_num', 'hard_disk', 'memory']
    d1, d2 = obj1, dict(obj2.iterlists())
    info = {}
    for k, v in d1.items():
        if k in fields:
            if d2.get(k):
                d2_value = d2[k]
            else:
                d2_value = u''
        elif k in no_check_fields:
            continue
        else:
            d2_value = d2[k][0]
        if not v:
            if v==False:
                pass
            else:
                v = u''
        if isinstance(v,list):
            v.sort()
            if not d2_value:
                d2_value = []
            d2_value.sort()
            if v != d2_value:
                info.update({k: [v, d2_value]})
        else:
            if str(v) != str(d2_value):
                info.update({k: [v, d2_value]})

    for k, v in info.items():
        if v == [None, u'']:
            info.pop(k)
    return info




@login_required
def host_edit(request):
    """ 修改主机 """
    uuid = request.GET.get('uuid')
    host = get_object_or_404(Host, uuid=uuid)
    uf = HostForm(instance=host)
    project_all = Project.objects.all()
    project_host = host.business.all()
    projects = [p for p in project_all if p not in project_host]

    service_all = Service.objects.all()
    service_host = host.service.all()
    services = [s for s in service_all if s not in service_host]
    username = request.user.username
    if request.method == 'POST':
        physics = request.POST.get('physics', '')
        uf_post = HostForm(request.POST, instance=host)
        if uf_post.is_valid():
            zw = uf_post.save(commit=False)
            zw.mac = str(request.POST.getlist("mac")[0]).replace(':', '-').strip(" ")
            request.POST = request.POST.copy()
            if physics:
                physics_host = get_object_or_404(Host, eth1=physics)
                request.POST['vm'] = physics_host.uuid
                if host.vm:
                    if str(host.vm.eth1) != str(physics):
                        zw.vm = physics_host
                else:
                    zw.vm = physics_host
                zw.type = 1
            else:
                request.POST['vm'] = ''
                zw.type = 0

            zw.save()
            uf_post.save_m2m()
            new_host = get_object_or_404(Host, uuid=uuid)
            info = get_diff(uf_post.__dict__.get('initial'), request.POST)
            db_to_record(username, host, info)
            return HttpResponseRedirect('/assets/host_detail/?uuid=%s' % uuid)

    return render(request,'assets/host_edit.html', locals())


@login_required
@csrf_exempt
def host_edit_batch(request):
    """ 批量修改主机 """
    uf = HostForm()
    username = request.user.username
    projects = Project.objects.all()
    services = Service.objects.all()
    if request.method == 'POST':
        ids = str(request.GET.get('uuid', ''))
        env = request.POST.get('env', '')
        idc = request.POST.get('idc', '')
        brand = request.POST.get('brand', '')
        business = request.POST.getlist('business', '')
        services = request.POST.getlist('service', '')
        cabinet = request.POST.get('cabinet', '')
        editor = request.POST.get('editor', '')
        uuid_list = ids.split(",")

        for uuid in uuid_list:
            record_list = []
            host = get_object_or_404(Host, uuid=uuid)
            if env:
                if not host.env:
                    info = u'无'
                else:
                    info = host.env
                if env != host.env:
                    text = u'环境' + u'由 ' + info + u' 更改为 ' + env
                    record_list.append(text)
                    host.env = env

            if idc:
                get_idc = get_object_or_404(IDC, uuid=idc)

                if host.idc != get_idc.name:
                    if not host.idc:
                        text = u'IDC' + u'由 ' + "none" + u' 更改为 ' + get_idc.name
                    else:
                        text = u'IDC' + u'由 ' + host.idc.name + u' 更改为 ' + get_idc.name
                    record_list.append(text)
                    host.idc = get_idc

            if brand:
                if brand != host.brand:
                    text = u'硬件厂商' + u'由 ' + host.brand + u' 更改为 ' + brand
                    record_list.append(text)
                    host.brand = brand

            if business:
                old, new, project_list = [], [], []
                for s in host.business.all():
                    project_name = s.service_name
                    old.append(project_name)
                for s in business:
                    project = Project.objects.get(uuid=s)
                    project_name = project.service_name
                    new.append(project_name)
                    project_list.append(project)
                if old != new:
                    text = u'所属业务' + u'由 ' + ','.join(old) + u' 更改为 ' + ','.join(new)
                    record_list.append(text)
                    host.business = project_list

            if services:
                old, new, service_list = [], [], []
                for s in host.service.all():
                    service_name = s.name
                    old.append(service_name)
                for s in services:
                    service = Service.objects.get(uuid=s)
                    service_name = service.name
                    new.append(service_name)
                    service_list.append(service)
                if old != new:
                    text = u'运行服务' + u'由 ' + ','.join(old) + u' 更改为 ' + ','.join(new)
                    record_list.append(text)
                    host.service = service_list

            if cabinet:
                if not host.cabinet:
                    info = u'无'
                else:
                    info = host.cabinet
                if cabinet != host.cabinet:
                    text = '机柜号' + u'由 ' + info + u' 更改为 ' + cabinet
                    record_list.append(text)
                    host.cabinet = cabinet

            if editor:
                if editor != host.editor:
                    text = '备注' + u'由 ' + host.editor + u' 更改为 ' + editor
                    record_list.append(text)
                    host.editor = editor

            if len(record_list) != 0:
                host.save()
                HostRecord.objects.create(host=host, user=username, content=record_list)

        return render(request,'assets/host_edit_batch_ok.html', locals())
    return render(request,'assets/host_edit_batch.html', locals())


@login_required
def host_detail(request):
    """ 主机详情 """
    uuid = request.GET.get('uuid', '')
    ip = request.GET.get('ip', '')
    if uuid:
        host = get_object_or_404(Host, uuid=uuid)
    elif ip:
        host = get_object_or_404(Host, eth1=ip)
    host_record = HostRecord.objects.filter(host=host).order_by('-time')
    return render(request,'assets/host_detail.html', locals())


@login_required
def host_del(request):
    """ 删除主机 """
    uuid = request.GET.get('uuid', '')
    host = get_object_or_404(Host, uuid=uuid)
    host.status = 3
    host.eth1 = ''
    host.eth2 = ''
    host.node_name = host.uuid
    host.internal_ip = ''
    host.system = ''
    host.system_cpuarch = ''
    host.system_version = ''
    host.cabinet = ''
    host.server_cabinet_id = 0
    host.env = ''
    host.number = ''
    host.switch_port = ''
    idc_ = IDC.objects.filter(name=u"报废库房")
    if idc_.exists():
        idc_ = idc_.first()
    else:
        idc_ = None
    host.idc = idc_
    host.business.clear()
    host.service.clear()
    host.save()
    return HttpResponseRedirect('/assets/host_list/')


@login_required
def host_del_batch(request):
    """ 批量删除主机 """
    ids = str(request.POST.get('ids'))
    for uuid in ids.split(','):
        host = get_object_or_404(Host, uuid=uuid)
        host.status = 3
        host.eth1 = ''
        host.eth2 = ''
        host.node_name = host.uuid
        host.internal_ip = ''
        host.system = ''
        host.system_cpuarch = ''
        host.system_version = ''
        host.cabinet = ''
        host.server_cabinet_id = 0
        host.env = ''
        host.number = ''
        host.switch_port = ''
        idc_ = IDC.objects.filter(name=u"报废库房")
        if idc_.exists():
            idc_ = idc_.first()
        else:
            idc_ = None
        host.idc = idc_
        host.business.clear()
        host.service.clear()
        host.save()
    return HttpResponseRedirect('/assets/host_list/')

