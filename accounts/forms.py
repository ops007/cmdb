from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.forms import models

from users.models import CustomUser
from accounts.models import *


class RegisterForm(forms.Form):
    email = forms.EmailField(label = '邮箱', max_length = 254, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    username = forms.CharField(label = '用户名', max_length = 30, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    password = forms.CharField(label = '密码', max_length = 30, widget = forms.PasswordInput(attrs = {'class': 'form-control'}))
    password_verify = forms.CharField(label = '密码验证', max_length = 30, widget = forms.PasswordInput(attrs = {'class': 'form-control'}))

    # class META:
    #     # 与models建立依赖关系
    #     model = UserCreateForm
    #     # 字段
    #     fields = ['username', 'email','password']
    #     # 排除字段
    #     exclude = None,
    #     # 帮助提示信息
    #     help_texts = {
    #         'username': '请输入用户名',
    #         'email': '请输入电子邮箱地址',
    #         'password': '请输入密码',
    #                  },

class LoginForm(forms.Form):
    username = forms.CharField(label = '用户名', max_length = 30, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    password = forms.CharField(label = '密码', max_length = 30, widget = forms.PasswordInput(attrs = {'class': 'form-control'}))

    class META:
        # 与models建立依赖关系
        model = UserCreateForm
        # 字段
        fields = ['username', 'password']
        # 排除字段
        exclude = None,
