# coding=utf-8
from django.db import models


class Country(models.Model):
    RATING_HELP = u'место в рейтинге, чем меньше, тем лучше'

    name = models.CharField(u'Страна', max_length=255, db_index=True)
    business = models.TextField(u'Бизнес иммиграция', null=True, blank=True)
    investor = models.TextField(u'ПМЖ для инвесторов', null=True, blank=True)
    pension = models.TextField(u'Рантье', null=True, blank=True)
    visa_run = models.TextField(u'Visa-run', null=True, blank=True)
    specialist = models.TextField(u'Профессиональная иммиграция', help_text=u'Балльная система либо признние диплома', null=True, blank=True)
    happiness = models.PositiveSmallIntegerField(u'Международный индекс счастья', help_text=RATING_HELP, null=True, blank=True)
    prosperity = models.PositiveSmallIntegerField(u'Prosperity Index Rank', help_text=RATING_HELP, null=True, blank=True)
    medicine = models.PositiveSmallIntegerField(u'Медицина (WHO rank)', help_text=RATING_HELP, null=True, blank=True)
    criminal = models.TextField(u'Криминал', null=True, blank=True)
    summer = models.SmallIntegerField(u'Средняя температура летом', null=True, blank=True)
    winter = models.SmallIntegerField(u'Средняя температура зимой', null=True, blank=True)
    mountains = models.NullBooleanField(u'Горы', blank=True, null=True)
    sea = models.NullBooleanField(u'Море', blank=True, null=True)
    rent = models.PositiveSmallIntegerField(u'Аренда', help_text=u'Дом или квартира среднего уровня', blank=True, null=True)
    language = models.TextField(u'Язык', null=True, blank=True)
    additional = models.TextField(u'Дополнительные плюшки', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Blog(models.Model):
    country = models.ForeignKey(Country)
    url = models.URLField(u'URL')
    name = models.CharField(u'Имя', max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name

