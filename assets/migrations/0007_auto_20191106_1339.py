# Generated by Django 2.2.6 on 2019-11-06 13:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20191022_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitcode',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9d245b-0057-11ea-9477-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9b7923-0057-11ea-9d28-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='hostrecord',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9d245a-0057-11ea-99bb-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='idc',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9b2b38-0057-11ea-bd15-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='iplist',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9d9930-0057-11ea-8313-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9b0442-0057-11ea-b4d1-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9b0443-0057-11ea-b975-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='project_swan',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9d4b46-0057-11ea-8755-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9b50c0-0057-11ea-93a8-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='publishingsystem',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9b2b39-0057-11ea-bfc1-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9b7922-0057-11ea-b589-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='zabbixrecord',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('cf9d723a-0057-11ea-bddf-24f6770d0683'), max_length=64, unique=True),
        ),
    ]
