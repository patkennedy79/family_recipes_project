# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('rating', models.PositiveIntegerField(max_length=5, default=1)),
                ('recipe_type', models.CharField(choices=[('BR', 'Breakfast'), ('LU', 'Lunch'), ('DI', 'Dinner'), ('DE', 'Dessert')], max_length=2, default='DI')),
            ],
        ),
    ]
