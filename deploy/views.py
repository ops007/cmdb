from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
# @login_required
from assets.models import Project,Line
from deploy.forms import DeployForm


def index(request):
    uf = DeployForm()
    projects = Project.objects.all()
    line = Line.objects.all()
    return render(request, 'deploy/index.html',locals())