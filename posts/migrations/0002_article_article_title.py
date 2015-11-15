# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_title',
            field=models.CharField(default='Blaap', max_length=100),
            preserve_default=False,
        ),
    ]
