from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
from .forms import *
from users.models import CustomUser
from django.contrib.auth import login, logout, authenticate

# 首页
@login_required
def index(request):
    return render(request,'user/index.html',locals())

# 注册
def userregister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = form.data.get('username')
        email = form.data.get('email')
        password = form.data.get('password')
        password_verify = form.data.get('password_verify')
        if password == password_verify:
            CustomUser.objects.create_user(username = username, email = email, password = password)
            return redirect('/accounts/login')
        else:
            message = '密码校验失败'
            return render(request, 'user/register.html', locals())
    else:
        form = RegisterForm()
        return render(request, 'user/register.html', locals())



# 登陆
def userlogin(request):
    redirect_to = request.GET.get('next', '')
    print(redirect_to)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            # user = authenticate(username = username, password = password)
            try:
                data = CustomUser.objects.get(username = username)
                print(data)
                if data:
                    check_data = check_password(password,data.password)
                    print(check_data,"aaa")
                    print(111)
                    if check_data:
                        data.backend = 'django.contrib.auth.backends.ModelBackend'
                        login(request, data)
                        # return redirect('/accounts/')
                        try:
                            if redirect_to:
                                return redirect(redirect_to)
                            else:
                                return redirect('/accounts/')
                        except:
                            return render(request, 'user/login.html', locals())
                    else:
                        message = "密码错误"
                        return render(request, 'user/login.html', locals())
            except:
                message = "登陆失败，用户名错误"
                return render(request, 'user/login.html', locals())

    form = LoginForm()
    return render(request, 'user/login.html', locals())


def userlogout(request):
    # request.session.flush()
    logout(request)  # 这种方式实现退出用户
    return redirect('/accounts/login/')
