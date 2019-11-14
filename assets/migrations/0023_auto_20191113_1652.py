# Generated by Django 2.2.6 on 2019-11-13 16:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0022_auto_20191113_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitcode',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05d0a34-05f2-11ea-85fb-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05d0a32-05f2-11ea-a079-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='hostrecord',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05d0a33-05f2-11ea-b576-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='idc',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05d0a2e-05f2-11ea-8f63-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='iplist',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05d0a37-05f2-11ea-9dd5-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='line',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05aa6cb-05f2-11ea-9b12-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05aa6cc-05f2-11ea-8da4-24f6770d0683'), max_length=64),
        ),
        migrations.AlterField(
            model_name='project_swan',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05d0a35-05f2-11ea-9cc4-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05d0a30-05f2-11ea-b855-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='publishingsystem',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05d0a2f-05f2-11ea-8823-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05d0a31-05f2-11ea-895c-24f6770d0683'), max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='zabbixrecord',
            name='uuid',
            field=models.CharField(auto_created=True, default=uuid.UUID('f05d0a36-05f2-11ea-b486-24f6770d0683'), max_length=64, unique=True),
        ),
    ]
