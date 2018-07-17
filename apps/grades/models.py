from __future__ import unicode_literals

from django.db import models
from ..courses.models import Course
from ..users.models import User

# Create your models here.
class Grade(models.Model):
  user = models.ForeignKey(User, related_name = "grades")
  course = models.ForeignKey(Course, related_name = "grades")
  grade = models.FloatField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)