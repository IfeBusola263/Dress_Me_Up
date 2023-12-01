#!/usr/bin/python3
"""This module implements the events end points for viewing all
available events on the website.
"""

from models import storage
from os import getenv
from flask import jsonify
from api.v1.views import app_views
from models.event import Event


@app_views.route('/events', strict_slashes=False, methods=['GET'])
def all_events():
    """This function returns all the events in the database.
    """
    # List of event objects
    evnt_to_disply = []
    events = storage.all(Event)
    for event in events.values():
        evnt_to_display.append(event)
