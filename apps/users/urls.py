from django.conf.urls import url
from . import views

urlpatterns = [
  url('^$', views.index, name='index'),
  url('^new/$', views.new, name='new'),
  url('^create/$', views.create, name='create'),
  url('^login/$', views.login, name='login')
]