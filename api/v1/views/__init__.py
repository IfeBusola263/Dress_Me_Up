#!/usr/bin/python3
"""Sets up Blueprint for the flask app"""

from flask import Blueprint

app_views = Blueprint('app_views',
                      __name__,
                      url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.user import *
