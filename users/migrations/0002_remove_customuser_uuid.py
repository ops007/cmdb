# Generated by Django 2.2.6 on 2019-10-16 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='uuid',
        ),
    ]
