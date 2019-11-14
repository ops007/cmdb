from deploy.models import Deploy
from django import forms


class DeployForm(forms.ModelForm):
    class Meta:
        model = Deploy
        fields = {"line", 'cluster','project', 'content'}