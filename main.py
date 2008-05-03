#!/usr/bin/env python

import wsgiref.handlers
from shifteleven import handlers
from shifteleven.handlers import project
from google.appengine.ext import webapp

context = '/v1'

class SiteRedirector(webapp.RequestHandler):
  def get(self):
    self.redirect(context)

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
        (context, handlers.MainHandler),
        ('%s/projects' % context, project.ProjectCollectionHandler),
        ('%s/projects/new' % context, project.NewProjectHandler),
        ('%s/projects/(\d+)' % context, project.ProjectHandler),
        ('%s/projects/(\d+)/edit' % context, project.EditProjectHandler)
      ],
      debug=True)
  wsgiref.handlers.CGIHandler().run(MockHTTPMethodMiddleware(application))

if __name__ == '__main__':
  main()
