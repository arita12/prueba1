from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    url(r'^$',inicio_view, name='Inicio'),
)