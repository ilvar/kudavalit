from django.contrib import admin

from countries.models import Country, Blog


class BlogInline(admin.TabularInline):
    model = Blog


class CountryAdmin(admin.ModelAdmin):
    inlines = [BlogInline]

admin.site.register(Country, CountryAdmin)
