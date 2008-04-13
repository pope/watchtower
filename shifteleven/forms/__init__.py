#!/usr/bin/env python

from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms
from shifteleven import models

class ProjectForm(djangoforms.ModelForm):
  class Meta:
    model = models.Project