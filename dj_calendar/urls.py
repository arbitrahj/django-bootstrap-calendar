# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from dj_calendar.views import CalendarJsonListView, CalendarView

urlpatterns = patterns('dj_calendar.views',
                       url(
                           r'^json/$',
                           CalendarJsonListView.as_view(),
                           name='calendar_json'
                       ),
                       url(
                           r'^$',
                           CalendarView.as_view(),
                           name='calendar'
                       ),
                       )
