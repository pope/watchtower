#!/usr/bin/env python

from google.appengine.api import users
from google.appengine.ext import webapp,db
from google.appengine.ext.webapp import template
from shifteleven import forms
from shifteleven import models

def findProject(id):
  return models.Project.get_by_id(int(id))

class ProjectCollectionHandler(webapp.RequestHandler):
  def get(self):
    """A list of all the projects"""
    projects = models.Project.all().filter("owner =", users.get_current_user()).fetch(100)
    self.response.out.write(
        template.render('shifteleven/views/project/index.html', {'projects': projects}))
  
  def post(self):
    """Create the new project.  Redirect to the newly created project page"""
    project_form = forms.ProjectForm(data=self.request.POST)
    if project_form.is_valid():
      project = project_form.save()
      self.redirect(ProjectHandler.get_url(project.key().id()))
    else:
      self.response.out.write(
          template.render('shifteleven/views/project/new.html', {'project_form': project_form}))

class NewProjectHandler(webapp.RequestHandler):
  def get(self):
    """Form for creating a new project"""
    project_form = forms.ProjectForm()
    self.response.out.write(
        template.render('shifteleven/views/project/new.html', {'project_form': project_form}))

class ProjectHandler(webapp.RequestHandler):
  def get(self, id):
    """Show the details of a project"""
    project = findProject(id)
    self.response.out.write(
        template.render('shifteleven/views/project/show.html', {'project': project}))
  
  def post(self, id):
    """Update the project.  Redirect to the updated project page"""
    project = findProject(id)
    project_form = forms.ProjectForm(data=self.request.params, instance=project)
    if project_form.is_valid():
      project = project_form.save()
      self.redirect(ProjectHandler.get_url(project.key().id()))
    else:
      self.response.out.write(
          template.render('shifteleven/views/project/edit.html', {'project': project, 'project_form': project_form}))
  
  def delete(self, id):
    """Delete the project"""
    findProject(id).delete()
    self.redirect(ProjectCollectionHandler.get_url())

class EditProjectHandler(webapp.RequestHandler):
  def get(self, id):
    """Form for editing the project"""
    project = findProject(id)
    project_form = forms.ProjectForm(instance=project)
    self.response.out.write(
        template.render('shifteleven/views/project/edit.html', {'project': project, 'project_form': project_form}))
