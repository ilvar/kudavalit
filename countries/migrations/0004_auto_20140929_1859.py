# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_auto_20140929_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='summer',
            field=models.SmallIntegerField(null=True, verbose_name='\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043b\u0435\u0442\u043e\u043c', blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='winter',
            field=models.SmallIntegerField(null=True, verbose_name='\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u0437\u0438\u043c\u043e\u0439', blank=True),
        ),
    ]
