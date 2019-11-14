# Generated by Django 2.2.6 on 2019-11-12 14:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20191112_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uuid',
            field=models.CharField(default=uuid.UUID('4f0d63b4-0514-11ea-9b6e-24f6770d0683'), max_length=64, unique=True),
        ),
    ]
