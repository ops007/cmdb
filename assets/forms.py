# coding:utf-8
from django import forms
from assets.models import Host, IDC, Service, Project
from users.models import department_Mode, CustomUser


class business_form(forms.ModelForm):
    # FAVORITE_COLORS_CHOICES = CustomUser.objects.values_list("id", "first_name",)
    # service_user = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    # Service_checkbox = Service.objects.values_list("id", "name",)
    # service = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=Service_checkbox)
    try:
        dev_group = department_Mode.objects.get(desc_gid=1003)
        FAVORITE_COLORS_CHOICES = CustomUser.objects.values_list("id", "first_name").filter(department_id=dev_group.id)
        # FAVORITE_COLORS_CHOICES = CustomUser.objects.values_list("id", "first_name")
        project_user_group = forms.MultipleChoiceField(required=False, widget=forms.SelectMultiple,
                                                       choices=FAVORITE_COLORS_CHOICES, label=u"用户列表")
    # project_user_group = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES, label=u"用户列表")
    except:
        pass

    class Meta:
        model = Project
        fields = ["service_name",
                  # "service_user",
                  "aliases_name",
                  "project_contact",
                  "project_contact_backup",
                  "description",
                  "line",
                  "project_user_group",
                  "sort",
                  ]

    def save(self, commit=False):
        instance = super(business_form, self).save(commit=True)
        # service_ids = self.cleaned_data.get('service')
        # service_list = Service.objects.filter(id__in=service_ids)
        # for one in service_list:
        #     _, o = ServiceMyForm.objects.get_or_create(business=instance, service=one)
        instance.save()
        return instance


class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ["node_name", "idc", "room_number", "eth1", "mac", "internal_ip", "room_number", "cabinet",
                  "server_cabinet_id", "number", "business", "service", "env", "status",
                  "cpu", "hard_disk", "memory", "system", "system_cpuarch", "vm", "Services_Code",
                  "brand", "guarantee_date", "server_sn", "idle", "editor"]


class IdcForm(forms.ModelForm):
    class Meta:
        model = IDC
        fields = ['name', "bandwidth", "operator", 'type', 'linkman', 'phone', 'network', 'address', 'comment']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'port', 'remark']


class Project_docForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["description"]
