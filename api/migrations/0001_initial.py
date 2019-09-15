# Generated by Django 2.2.3 on 2019-08-07 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomSettingsScheduler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('type_of_task', models.TextField()),
                ('message_of_task', models.TextField()),
                ('list_members', models.TextField()),
                ('task_id', models.IntegerField()),
                ('time_field_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.TextField()),
                ('work_service', models.BooleanField()),
                ('login_mm', models.TextField()),
            ],
        ),
    ]
