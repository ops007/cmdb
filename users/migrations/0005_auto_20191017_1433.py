# Generated by Django 2.2.6 on 2019-10-17 14:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191017_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uuid',
            field=models.CharField(default=uuid.UUID('0fae81d8-f0a8-11e9-928e-24f6770d0683'), max_length=64, unique=True),
        ),
    ]
