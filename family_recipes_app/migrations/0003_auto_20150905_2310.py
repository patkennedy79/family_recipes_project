# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family_recipes_app', '0002_auto_20150831_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='images/', default='images/default_image.jpg'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='Add ingredients!'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_steps',
            field=models.TextField(default='Add recipe steps!'),
        ),
    ]
