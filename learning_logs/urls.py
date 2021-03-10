"""URL patterns for learning_log"""
from django.urls import re_path
from . import views #import the views from the current directory

app_name = "learning_logs"
urlpatterns = [
	
	re_path(r'^$', views.index, name = 'index'),
	re_path(r'^topics/$', views.topics, name = 'topics'),
	re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
	re_path(r'^new_topic/$', views.new_topic, name = 'new_topic'),
	re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name = 'new_entry'),
	re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = 'edit_entry'),
]