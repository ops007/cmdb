# Generated by Django 2.2.6 on 2019-11-13 16:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20191112_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uuid',
            field=models.CharField(default=uuid.UUID('9b2e3aca-05f1-11ea-b6bb-24f6770d0683'), max_length=64, unique=True),
        ),
    ]
