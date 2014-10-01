# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_auto_20140929_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('name', models.CharField(help_text='\u0427\u0442\u043e \u0437\u0430 \u0441\u0441\u044b\u043b\u043a\u0430 - \u041c\u0418\u0414, \u0432\u0438\u0437\u044b, etc', max_length=255, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('country', models.ForeignKey(to='countries.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='country',
            name='capital_iata',
            field=models.CharField(help_text='\u0414\u043b\u044f \u0441\u0431\u043e\u0440\u0430 \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u0438 \u0431\u0438\u043b\u0435\u0442\u043e\u0432', max_length=32, null=True, verbose_name='IATA code', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='flight_price',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u043e\u043b\u0435\u0442\u0430 \u0438\u0437 MOW', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='flight_time',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u043e\u043b\u0435\u0442\u0430 \u0438\u0437 MOW', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='language_english',
            field=models.NullBooleanField(help_text='50+% \u043d\u0430\u0441\u0435\u043b\u0435\u043d\u0438\u044f \u043c\u043e\u0433\u0443\u0442 \u043e\u0431\u044a\u044f\u0441\u043d\u0438\u0442\u044c\u0441\u044f \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u043c', verbose_name='\u041f\u043e\u043d\u0438\u043c\u0430\u044e\u0442 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='language_russian',
            field=models.NullBooleanField(help_text='50+% \u043d\u0430\u0441\u0435\u043b\u0435\u043d\u0438\u044f \u043c\u043e\u0433\u0443\u0442 \u043e\u0431\u044a\u044f\u0441\u043d\u0438\u0442\u044c\u0441\u044f \u043d\u0430 \u0440\u0443\u0441\u0441\u043a\u043e\u043c', verbose_name='\u041f\u043e\u043d\u0438\u043c\u0430\u044e\u0442 \u0440\u0443\u0441\u0441\u043a\u0438\u0439'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='numbeo_link',
            field=models.URLField(help_text='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0442\u043e\u043b\u0438\u0446\u0443 \u0432 numbeo.com', null=True, verbose_name='Numbeo', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='residence_min',
            field=models.PositiveSmallIntegerField(help_text='\u0421\u0430\u043c\u044b\u0439 \u0434\u0435\u0448\u0435\u0432\u044b\u0439 \u0432\u0430\u0440\u0438\u0430\u043d\u0442 \u041f\u041c\u0416 (\u043d\u0435 \u0441\u0442\u0443\u0434\u0435\u043d\u0442, \u043d\u0435 \u0432\u0438\u0437\u0430-\u0440\u0430\u043d\u044b)', null=True, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0440\u0435\u0437\u0438\u0434\u0435\u043d\u0446\u0438\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='residence_min_description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0434\u0435\u0448\u0435\u0432\u043e\u0439 \u0440\u0435\u0437\u0438\u0434\u0435\u043d\u0446\u0438\u0438', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='time_zone',
            field=models.SmallIntegerField(help_text='\u0426\u0435\u043b\u043e\u0435 \u0447\u0438\u0441\u043b\u043e \u0447\u0430\u0441\u043e\u0432 (\u043c\u043e\u0436\u043d\u043e \u043e\u043a\u0440\u0443\u0433\u043b\u0438\u0442\u044c), \u043f\u043e \u0413\u0440\u0438\u043d\u0432\u0438\u0447\u0443', null=True, verbose_name='\u0427\u0430\u0441\u043e\u0432\u043e\u0439 \u043f\u043e\u044f\u0441', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='visa_free_default',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='\u0412\u0438\u0437\u0430 \u043f\u043e \u043f\u0440\u0438\u043b\u0435\u0442\u0443 - \u0441\u0440\u043e\u043a', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='country',
            name='visa_free_max',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='\u0412\u0438\u0437\u0430 \u043f\u043e \u043f\u0440\u0438\u043b\u0435\u0442\u0443 - \u0434\u043e \u0441\u043a\u043e\u043b\u044c\u043a\u0438 \u043f\u0440\u043e\u0434\u043b\u0435\u0432\u0430\u0435\u0442\u0441\u044f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='rent',
            field=models.PositiveSmallIntegerField(help_text='\u0414\u043e\u043c \u0438\u043b\u0438 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u0430 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f', null=True, verbose_name='\u0410\u0440\u0435\u043d\u0434\u0430 \u0432 USD', blank=True),
        ),
    ]
