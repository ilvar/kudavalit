# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='rent',
            field=models.PositiveSmallIntegerField(help_text='\u0414\u043e\u043c \u0438\u043b\u0438 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u0430 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f', null=True, verbose_name='\u0410\u0440\u0435\u043d\u0434\u0430', blank=True),
        ),
    ]
