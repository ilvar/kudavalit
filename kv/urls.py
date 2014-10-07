from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('countries.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'country', name='country'),
    url(r'^help/$', 'help_page', name='help'),
    url(r'^add/$', 'add_page', name='add'),
    url(r'^upload/$', 'upload', name='upload'),
    url(r'^update_prices/$', 'update_prices', name='update_prices'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
