# Generated by Django 2.2.6 on 2019-10-22 15:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20191022_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitcode',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f8c065-f49c-11e9-9698-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='service',
            field=models.ManyToManyField(blank=True, to='assets.Service', verbose_name='运行服务'),
        ),
        migrations.AlterField(
            model_name='host',
            name='type',
            field=models.IntegerField(blank=True, default=1, verbose_name='主机类型'),
        ),
        migrations.AlterField(
            model_name='host',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f713de-f49c-11e9-af58-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='hostrecord',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f8c064-f49c-11e9-b755-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='idc',
            name='operator',
            field=models.IntegerField(blank=True, choices=[(0, '电信'), (1, '联通'), (2, '移动'), (3, '铁通'), (4, '小带宽')], null=True, verbose_name='运营商'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='type',
            field=models.IntegerField(blank=True, choices=[(0, 'CDN'), (1, '核心')], null=True, verbose_name='机房类型'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f6ece8-f49c-11e9-9c33-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='iplist',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f90e51-f49c-11e9-b287-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='sort',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='line',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f69f02-f49c-11e9-a6f6-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f6c5f8-f49c-11e9-9c58-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='project_swan',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f8c066-f49c-11e9-b1fd-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f713dc-f49c-11e9-a368-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='publishingsystem',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f6ece9-f49c-11e9-871b-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f713dd-f49c-11e9-8516-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='zabbixrecord',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('34f90e50-f49c-11e9-a156-24f6770d0683'), max_length=64, unique=True),
        ),
    ]
