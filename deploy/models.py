from django.db import models

# Create your models here.
from accounts import forms
from assets.models import Line, Project
import uuid


class Deploy(models.Model):
    uuid = models.CharField(max_length=64, auto_created = True, unique=True, default = uuid.uuid1())
    line = models.ForeignKey(Line, blank=True, null=True, verbose_name=u'产品线', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, blank=True, null=True, verbose_name=u'项目', on_delete=models.CASCADE)
    cluster = models.CharField(max_length=64, auto_created = True, default = None)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,verbose_name=u'内容', null=True)
    def __unicode__(self):
        return self.uuid
    class Meta:
        verbose_name = u'部署'
        verbose_name_plural = verbose_name
        app_label = 'deploy'