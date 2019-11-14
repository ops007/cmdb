from django import forms
from users.models import CustomUser

# Create your models here.
class UserCreateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'email', 'department', 'mobile', "user_key")