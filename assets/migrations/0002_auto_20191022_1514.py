# Generated by Django 2.2.6 on 2019-10-22 15:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitcode',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a6e469-f49b-11e9-ae0e-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.IDC', verbose_name='机房'),
        ),
        migrations.AlterField(
            model_name='host',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a55ed4-f49b-11e9-a33b-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='hostrecord',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a6e468-f49b-11e9-8b4c-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='idc',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a510e4-f49b-11e9-bfbf-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='iplist',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a7593a-f49b-11e9-8fd9-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a4e8ba-f49b-11e9-a3b8-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a4e8bb-f49b-11e9-a281-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='project_swan',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a70b52-f49b-11e9-87ba-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a537e3-f49b-11e9-af12-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='publishingsystem',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a537e2-f49b-11e9-9c18-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a537e4-f49b-11e9-90cf-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='zabbixrecord',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('91a7325c-f49b-11e9-8421-24f6770d0683'), max_length=64, unique=True),
        ),
    ]