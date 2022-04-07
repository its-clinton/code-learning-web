from unicodedata import name
from django import views
from django.urls import path
from . import views
from . views import *

app_name = 'core'

urlpatterns = [
    path('', views.index_view, name='index_view'),
]
