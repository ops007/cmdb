# Generated by Django 2.2.6 on 2019-11-12 16:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20191112_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uuid',
            field=models.CharField(default=uuid.UUID('aba8f6ee-0525-11ea-bd37-24f6770d0683'), max_length=64, unique=True),
        ),
    ]
