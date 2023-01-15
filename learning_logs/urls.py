"""Defines URL patterns for learning_logs."""

from django.conf.urls import include
from . import views
from django.urls import path

app_name = "learning_logs"

urlpatterns = [
    path(r'',views.index,name="index"),
    path('topics/',views.topics,name="topics"),
    path(r'topics/<topic_id>/',views.topic,name="topic"),
    path(r'new_topic/',views.new_topic, name = "new_topic"),
    path(r'new_entry/<topic_id>/',views.new_entry,name = "new_entry"),
    path(r'edit_entry/<entry_id>/',views.edit_entry,name = "edit_entry"),
]