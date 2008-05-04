#!/usr/bin/env python

from functools import update_wrapper
from google.appengine.api import users
from google.appengine.ext import webapp

def login_required(f):
  def _f(self, *a, **kw):
    user = users.get_current_user()
    if not user:
      self.redirect(users.create_login_url(self.request.url))
    else:
      f(self, *a, **kw)
  return update_wrapper(_f, f)

class MainHandler(webapp.RequestHandler):
  """Handles the home page."""
  def get(self):
    self.response.out.write('Hello world!')

