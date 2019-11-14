import ast

from django import template
from assets.models import Host, Project
register = template.Library()

@register.filter(name='business_list')
def business_list(host):
    cmdb_data = Host.objects.get(pk=host)
    data = cmdb_data.business.all()

    business_all = []
    for i in data:
        business_all.append(i.service_name)

    return business_all