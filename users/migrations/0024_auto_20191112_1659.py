# Generated by Django 2.2.6 on 2019-11-12 16:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20191112_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uuid',
            field=models.CharField(default=uuid.UUID('bf0aec80-052a-11ea-a56c-24f6770d0683'), max_length=64, unique=True),
        ),
    ]
