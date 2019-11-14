from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render



@login_required
def index(request):
    return redirect('/accounts/')

def t(request):
    return render(request,'t.html',locals())

def t2(request):
    return render(request,'t2.html',locals())