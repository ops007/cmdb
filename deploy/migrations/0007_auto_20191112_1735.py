# Generated by Django 2.2.6 on 2019-11-12 17:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0006_auto_20191112_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deploy',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='deploy',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('b5850bc6-052f-11ea-9da7-24f6770d0683'), max_length=64, unique=True),
        ),
    ]