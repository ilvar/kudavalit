from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('countries.views',
    url(r'^$', 'index', name='index'),
    url(r'^help/$', 'help_page', name='help'),
    url(r'^add/$', 'add_page', name='add'),
    url(r'^upload/$', 'upload', name='upload'),


    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)