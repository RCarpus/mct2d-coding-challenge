# task_tracker/urls.py

from django.urls import path
from . import views

app_name = 'task_tracker'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('submission-list', views.submission_list, name='submission_list'),
    path('submission-list-new', views.submission_new_type_list,
         name='submission_new_list'),
    path('task-submission/<int:task_id>/',
         views.task_submission_form_view, name='task_submission'),
    path('task-submission-new/<int:task_id>/',
         views.task_submission_new_type_form_view, name='task_submission_new'),
]
