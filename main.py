#!/usr/bin/env python

import wsgiref.handlers
from shifteleven import handlers
from shifteleven.handlers import project
from google.appengine.ext import webapp
import request

class SiteRedirector(webapp.RequestHandler):
  def get(self):
    self.redirect('/v1')

class MockHTTPMethodMiddleware(object):
  def __init__(self, app):
    self.app = app

  def __call__(self, environ, start_response):
    method = webapp.Request(environ).get('_method')
    if method:
      environ['REQUEST_METHOD'] = method.upper()
    return self.app(environ, start_response)

def main():
  application = webapp.WSGIApplication([
        ('/', SiteRedirector),
        ('/v1', handlers.MainHandler),
        ('/v1/projects', project.ProjectCollectionHandler),
        ('/v1/projects/new', project.NewProjectHandler),
        ('/v1/projects/(\d+)', project.ProjectHandler),
        ('/v1/projects/(\d+)/edit', project.EditProjectHandler)
      ],
      debug=True)
  wsgiref.handlers.CGIHandler().run(MockHTTPMethodMiddleware(application))

if __name__ == '__main__':
  main()
