# Generated by Django 2.0 on 2019-12-11 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelform_demo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='BookDemo',
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='UserDemo',
        ),
    ]