# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='virtual_machine_type_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('virtual_machine_type_name', models.CharField(max_length=200)),
                ('cpu_cores_required', models.CharField(max_length=200)),
                ('ram_required', models.CharField(max_length=200)),
                ('minimum_network_required', models.CharField(max_length=200)),
                ('maximum_network_required', models.CharField(max_length=200)),
                ('virtual_network_function_instance_type_id', models.CharField(max_length=200)),
                ('cpu_pin', models.CharField(max_length=200)),
                ('cross_socket_pin', models.CharField(max_length=200)),
            ],
        ),
    ]
