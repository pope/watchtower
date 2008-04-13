#!/usr/bin/env python

from google.appengine.ext import db
from google.appengine.api import users

class Project(db.Model):
  name = db.StringProperty(required=True)
  owner = db.UserProperty(required=True)