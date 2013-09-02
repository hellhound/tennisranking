# -*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView, TemplateView

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/ranking/'),
    name='home'),
    url(r'^ranking/$', TemplateView.as_view(template_name='ranking/ranking.html'),
    name='ranking'),
    url(r'^duels/$', TemplateView.as_view(template_name='ranking/duels.html'),
    name='duels'),
)
