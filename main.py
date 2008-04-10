#!/usr/bin/env python

import wsgiref.handlers
from shifteleven import handlers
from google.appengine.ext import webapp

def main():
  application = webapp.WSGIApplication([('/', handlers.MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
