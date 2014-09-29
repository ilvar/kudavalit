from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('countries.views',
    url(r'^$', 'index', name='index'),
    url(r'^help/$', 'help_page', name='help'),
    url(r'^add/$', 'add_page', name='add'),
    url(r'^upload/$', 'upload', name='upload'),


    url(r'^admin/', include(admin.site.urls)),
)
