from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.core import serializers
import json
from .models import User

# Create your views here.
def index(req):
  return render(req, 'users/index.html')

def new(req):
  return render(req, 'users/new.html')

def create(req):
  valid, result = User.objects.validate_and_create_user(req.POST)
  if not valid:
    response = {
      'errors': result
    }
    return HttpResponse(json.dumps(response), status=400)
  
  req.session['user_id'] = result.id
  return redirect('users:index')

def login(req):
  valid, result = User.objects.validate_login(req.POST)
  print "*" * 80
  print valid, result
  if not valid:
    for error in result:
      messages.error(req, error)
    return redirect('users:new')
  
  req.session['user_id'] = result.id
  return redirect('users:index')