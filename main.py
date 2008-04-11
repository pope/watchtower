#!/usr/bin/env python

import wsgiref.handlers
from shifteleven import handlers
from google.appengine.ext import webapp

class MockHTTPMethodMiddleware(object):
  def __init__(self, app):
    self.app = app

  def __call__(self, environ, start_response):
    method = webapp.Request(environ).get('_method')
    if method:
      environ['REQUEST_METHOD'] = method.upper()
    return self.app(environ, start_response)

def main():
  application = webapp.WSGIApplication([('/', handlers.MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(MockHTTPMethodMiddleware(application))

if __name__ == '__main__':
  main()
