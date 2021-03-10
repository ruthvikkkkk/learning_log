"""URL patterns for notes"""

from django.urls import re_path
from . import views

app_name = "notes"
urlpatterns = [
	
	re_path(r'^whatnotes/$', views.whatnotes, name = 'whatnotes'),
] 