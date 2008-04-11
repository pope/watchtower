#!/usr/bin/env python

from google.appengine.ext import webapp

class ProjectCollectionHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write('ProjectCollectionHandler GET')
  
  def post(self):
    pass

class NewProjectHandler(webapp.RequestHandler):
  def get(self):
    self.response.out.write('NewProjectHandler GET')

class ProjectHandler(webapp.RequestHandler):
  def get(self, id):
    self.response.out.write('ProjectHandler GET')
  
  def put(self, id):
    pass
  
  def delete(self, id):
    pass

class EditProjectHandler(webapp.RequestHandler):
  def get(self, id):
    self.response.out.write('EditProjectHandler GET')
