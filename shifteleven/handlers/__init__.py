#!/usr/bin/env python

from google.appengine.ext import webapp

class MainHandler(webapp.RequestHandler):
  """Handles the home page."""
  def get(self):
    self.response.out.write('Hello world!')

