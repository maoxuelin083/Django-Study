# Generated by Django 2.0 on 2019-12-11 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=100)),
                ('sex', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='related_demo.Users'),
        ),
    ]
