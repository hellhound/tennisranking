from django.conf.urls import patterns, include, url

import settings


urlpatterns = patterns('',
    url(r'', include('ranking.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
