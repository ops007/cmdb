# Generated by Django 2.2.6 on 2019-11-12 17:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20191112_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uuid',
            field=models.CharField(default=uuid.UUID('3b134458-052b-11ea-9628-24f6770d0683'), max_length=64, unique=True),
        ),
    ]