from django.contrib import admin

from countries.models import Country, Blog, Link


class BlogInline(admin.TabularInline):
    model = Blog


class LinkInline(admin.TabularInline):
    model = Link


class CountryAdmin(admin.ModelAdmin):
    inlines = [LinkInline, BlogInline]

admin.site.register(Country, CountryAdmin)
