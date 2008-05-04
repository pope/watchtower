#!/usr/bin/env python

from functools import update_wrapper
from google.appengine.api import users
from google.appengine.ext import webapp,db
from google.appengine.ext.webapp import template
from shifteleven import forms, handlers, models

def find_project(f):
  """Used to find a project by id.  Once found it passes the project on rather than the id"""
  def _f(self, id):
    project = models.Project.get_by_id(int(id))
    if project:
      f(self, project)
    else:
      self.error(404)
  return update_wrapper(_f, f)

class ProjectCollectionHandler(webapp.RequestHandler):
  @handlers.login_required
  def get(self):
    """A list of all the projects"""
    projects = models.Project.all().filter("owner =", users.get_current_user()).fetch(100)
    self.response.out.write(
        template.render('shifteleven/views/project/index.html', {'projects': projects}))

  @handlers.login_required
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
  @handlers.login_required
  def get(self):
    """Form for creating a new project"""
    project_form = forms.ProjectForm()
    self.response.out.write(
        template.render('shifteleven/views/project/new.html', {'project_form': project_form}))

class ProjectHandler(webapp.RequestHandler):
  @handlers.login_required
  @find_project
  def get(self, project):
    """Show the details of a project"""
    self.response.out.write(
        template.render('shifteleven/views/project/show.html', {'project': project}))

  @handlers.login_required
  @find_project
  def post(self, project):
    """Update the project.  Redirect to the updated project page"""
    project_form = forms.ProjectForm(data=self.request.params, instance=project)
    if project_form.is_valid():
      project = project_form.save()
      self.redirect(ProjectHandler.get_url(project.key().id()))
    else:
      self.response.out.write(
          template.render('shifteleven/views/project/edit.html', {'project': project, 'project_form': project_form}))

  @handlers.login_required
  @find_project
  def delete(self, project):
    """Delete the project"""
    project.delete()
    self.redirect(ProjectCollectionHandler.get_url())

class EditProjectHandler(webapp.RequestHandler):
  @handlers.login_required
  @find_project
  def get(self, project):
    """Form for editing the project"""
    project_form = forms.ProjectForm(instance=project)
    self.response.out.write(
        template.render('shifteleven/views/project/edit.html', {'project': project, 'project_form': project_form}))
