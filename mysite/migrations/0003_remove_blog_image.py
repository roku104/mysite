# Generated by Django 2.1.1 on 2018-09-26 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20180912_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]
