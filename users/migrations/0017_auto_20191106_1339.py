# Generated by Django 2.2.6 on 2019-11-06 13:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20191022_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='uuid',
            field=models.CharField(default=uuid.UUID('cf9a8df6-0057-11ea-9dcc-24f6770d0683'), max_length=64, unique=True),
        ),
    ]