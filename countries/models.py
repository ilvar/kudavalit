# coding=utf-8
from django.db import models


class Country(models.Model):
    RATING_HELP = u'место в рейтинге, чем меньше, тем лучше'

    name = models.CharField(u'Страна', max_length=255, db_index=True)

    # Visas
    business = models.TextField(u'Бизнес иммиграция', null=True, blank=True)
    investor = models.TextField(u'ПМЖ для инвесторов', null=True, blank=True)
    pension = models.TextField(u'Рантье', null=True, blank=True)
    visa_run = models.TextField(u'Visa-run', null=True, blank=True)
    specialist = models.TextField(u'Профессиональная иммиграция', help_text=u'Балльная система либо признние диплома', null=True, blank=True)

    visa_free_default = models.PositiveSmallIntegerField(u'Виза по прилету - срок', null=True, blank=True)
    visa_free_max = models.PositiveSmallIntegerField(u'Виза по прилету - до скольки продлевается', null=True, blank=True)
    residence_min = models.PositiveSmallIntegerField(u'Стоимость резиденции', null=True, blank=True, help_text=u'Самый дешевый вариант ПМЖ (не студент, не виза-раны)')
    residence_min_description = models.TextField(u'Описание дешевой резиденции', null=True, blank=True)

    # Ratings
    happiness = models.PositiveSmallIntegerField(u'Международный индекс счастья', help_text=RATING_HELP, null=True, blank=True)
    prosperity = models.PositiveSmallIntegerField(u'Prosperity Index Rank', help_text=RATING_HELP, null=True, blank=True)
    medicine = models.PositiveSmallIntegerField(u'Медицина (WHO rank)', help_text=RATING_HELP, null=True, blank=True)
    criminal = models.TextField(u'Криминал', null=True, blank=True)

    # Nature
    summer = models.SmallIntegerField(u'Средняя температура летом', null=True, blank=True)
    winter = models.SmallIntegerField(u'Средняя температура зимой', null=True, blank=True)
    mountains = models.NullBooleanField(u'Горы', blank=True, null=True)
    sea = models.NullBooleanField(u'Море', blank=True, null=True)

    # Prices
    rent = models.PositiveSmallIntegerField(u'Аренда в USD', help_text=u'Дом или квартира среднего уровня', blank=True, null=True)
    numbeo_link = models.URLField(u'Numbeo', blank=True, null=True, help_text=u'Ссылка на столицу в numbeo.com')

    # Transport
    capital_iata = models.CharField(u'IATA code', max_length=32, blank=True, null=True, help_text=u'Для сбора стоимости билетов')
    flight_time = models.PositiveSmallIntegerField(u'Время полета из MOW', blank=True, null=True)
    flight_price = models.PositiveSmallIntegerField(u'Стоимость полета из MOW', blank=True, null=True)
    time_zone = models.SmallIntegerField(u'Часовой пояс', help_text=u'Целое число часов (можно округлить), по Гринвичу', blank=True, null=True)

    # Languages
    language = models.TextField(u'Язык', null=True, blank=True)
    language_english = models.NullBooleanField(u'Понимают английский', blank=True, null=True, help_text=u'50+% населения могут объясниться на английском')
    language_russian = models.NullBooleanField(u'Понимают русский', blank=True, null=True, help_text=u'50+% населения могут объясниться на русском')

    # Other
    additional = models.TextField(u'Дополнительные плюшки', null=True, blank=True)

    def time_shift(self):
        if self.time_zone is not None:
            return abs(self.time_zone - 4)
        else:
            return

    @models.permalink
    def get_absolute_url(self):
        return 'country', [self.pk]

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


class Link(models.Model):
    country = models.ForeignKey(Country)
    url = models.URLField(u'URL')
    name = models.CharField(u'Описание', max_length=255, help_text=u'Что за ссылка - МИД, визы, etc')

    def __unicode__(self):
        return self.name
