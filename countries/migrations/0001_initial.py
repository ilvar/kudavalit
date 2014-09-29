# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('name', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0430')),
                ('business', models.TextField(null=True, verbose_name='\u0411\u0438\u0437\u043d\u0435\u0441 \u0438\u043c\u043c\u0438\u0433\u0440\u0430\u0446\u0438\u044f', blank=True)),
                ('investor', models.TextField(null=True, verbose_name='\u041f\u041c\u0416 \u0434\u043b\u044f \u0438\u043d\u0432\u0435\u0441\u0442\u043e\u0440\u043e\u0432', blank=True)),
                ('pension', models.TextField(null=True, verbose_name='\u0420\u0430\u043d\u0442\u044c\u0435', blank=True)),
                ('visa_run', models.TextField(null=True, verbose_name='Visa-run', blank=True)),
                ('specialist', models.TextField(help_text='\u0411\u0430\u043b\u043b\u044c\u043d\u0430\u044f \u0441\u0438\u0441\u0442\u0435\u043c\u0430 \u043b\u0438\u0431\u043e \u043f\u0440\u0438\u0437\u043d\u043d\u0438\u0435 \u0434\u0438\u043f\u043b\u043e\u043c\u0430', null=True, verbose_name='\u041f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u0438\u043c\u043c\u0438\u0433\u0440\u0430\u0446\u0438\u044f', blank=True)),
                ('happiness', models.PositiveSmallIntegerField(help_text='\u043c\u0435\u0441\u0442\u043e \u0432 \u0440\u0435\u0439\u0442\u0438\u043d\u0433\u0435, \u0447\u0435\u043c \u043c\u0435\u043d\u044c\u0448\u0435, \u0442\u0435\u043c \u043b\u0443\u0447\u0448\u0435', null=True, verbose_name='\u041c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0439 \u0438\u043d\u0434\u0435\u043a\u0441 \u0441\u0447\u0430\u0441\u0442\u044c\u044f', blank=True)),
                ('prosperity', models.PositiveSmallIntegerField(help_text='\u043c\u0435\u0441\u0442\u043e \u0432 \u0440\u0435\u0439\u0442\u0438\u043d\u0433\u0435, \u0447\u0435\u043c \u043c\u0435\u043d\u044c\u0448\u0435, \u0442\u0435\u043c \u043b\u0443\u0447\u0448\u0435', null=True, verbose_name='Prosperity Index Rank', blank=True)),
                ('medicine', models.PositiveSmallIntegerField(help_text='\u043c\u0435\u0441\u0442\u043e \u0432 \u0440\u0435\u0439\u0442\u0438\u043d\u0433\u0435, \u0447\u0435\u043c \u043c\u0435\u043d\u044c\u0448\u0435, \u0442\u0435\u043c \u043b\u0443\u0447\u0448\u0435', null=True, verbose_name='\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0430 (WHO rank)', blank=True)),
                ('criminal', models.TextField(null=True, verbose_name='\u041a\u0440\u0438\u043c\u0438\u043d\u0430\u043b', blank=True)),
                ('summer', models.PositiveSmallIntegerField(null=True, verbose_name='\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043b\u0435\u0442\u043e\u043c', blank=True)),
                ('winter', models.PositiveSmallIntegerField(null=True, verbose_name='\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u0437\u0438\u043c\u043e\u0439', blank=True)),
                ('mountains', models.NullBooleanField(verbose_name='\u0413\u043e\u0440\u044b')),
                ('sea', models.NullBooleanField(verbose_name='\u041c\u043e\u0440\u0435')),
                ('rent', models.PositiveSmallIntegerField(help_text='\u0414\u043e\u043c \u0438\u043b\u0438 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u0430 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f', verbose_name='\u0410\u0440\u0435\u043d\u0434\u0430')),
                ('language', models.TextField(null=True, verbose_name='\u042f\u0437\u044b\u043a', blank=True)),
                ('additional', models.TextField(null=True, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u043b\u044e\u0448\u043a\u0438', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='country',
            field=models.ForeignKey(to='countries.Country'),
            preserve_default=True,
        ),
    ]
