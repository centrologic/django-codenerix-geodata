# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-21 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_geodata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citygeonameen',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='citygeonamees',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='continentgeonameen',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='continentgeonamees',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='countrygeonameen',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='countrygeonamees',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='provincegeonameen',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='provincegeonamees',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='regiongeonameen',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='regiongeonamees',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
    ]