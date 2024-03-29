# Generated by Django 2.2.6 on 2019-11-13 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0021_auto_20191113_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitcode',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cec9a9-05f2-11ea-91d1-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cc673d-05f2-11ea-9e16-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='hostrecord',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cec9a8-05f2-11ea-959d-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='idc',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cc6739-05f2-11ea-acca-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='iplist',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cec9ac-05f2-11ea-8b0f-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cc6737-05f2-11ea-ac65-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cc6738-05f2-11ea-8b04-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='project_swan',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cec9aa-05f2-11ea-a05a-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cc673b-05f2-11ea-8af0-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='publishingsystem',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cc673a-05f2-11ea-9a3e-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cc673c-05f2-11ea-999d-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='zabbixrecord',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('58cec9ab-05f2-11ea-8c7b-24f6770d0683'), max_length=64, unique=True),
        ),
    ]
