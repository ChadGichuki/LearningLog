""" Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show All topics
    path('topics/', views.topics, name='topics'),

    # Detailed page for each topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for addding new topics
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for new entry
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),

    # Page for editing entries
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
