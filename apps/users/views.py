from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(req):
  return render(req, 'users/index.html')

def new(req):
  return render(req, 'users/new.html')

def create(req):
  errors = User.objects.validate_and_create_user(req.POST)
  if len(errors) > 0:
    for error in errors:
      messages.error(req, error)
    return redirect('users:new')
  return redirect('users:index')

def login(req):
  return redirect('users:index')