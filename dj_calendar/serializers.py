# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

import json
from datetime import datetime

from django.db.models.query import QuerySet
from dj_calendar.utils import datetime_to_timestamp
from dj_calendar.models import CalendarEvent


def event_serializer(events):
    """
    serialize event model
    """
    objects_body = []

    if isinstance(events, QuerySet):
        for event in events:
            field = {
                "id": event.pk,
                "title": event.title,
                "url": event.url,
                "class": event.css_class,
                "start": event.start_timestamp,
                "end": event.end_timestamp
            }
            objects_body.append(field)

    objects_head = {"success": 1}
    objects_head["result"] = objects_body
    return json.dumps(objects_head)

def pto_serializer(ptos):
    objects_body = []

    if isinstance(ptos, QuerySet):
        color_choices=len(CalendarEvent.CSS_CLASS_CHOICES)
        current_color=0

        for pto in ptos:
            field = {
                "id": pto.pk,
                "title": pto.user_profile.user.get_full_name() + " is out today.",
                "url": pto.get_absolute_url(),
                "class": CalendarEvent.CSS_CLASS_CHOICES[current_color][0], #todo coloring scheme by department/person/etc
                "start": datetime_to_timestamp( datetime.combine(pto.pto_start_date , datetime.min.time() )),
                "end":   datetime_to_timestamp( datetime.combine(pto.pto_end_date, datetime.min.time() ))
            }
            objects_body.append(field)
            if current_color+1 < color_choices:
                current_color += 1
            else:
                current_color = 0

    objects_head = {"success": 1}
    objects_head["result"] = objects_body
    return json.dumps(objects_head)
