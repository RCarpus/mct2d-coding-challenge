# task_tracker/urls.py

from django.urls import path
from . import views

app_name = 'task_tracker'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add-task/', views.add_task, name='add_task'),
    path('update-task/<int:task_id>', views.update_task, name="update_task"),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('submission-list', views.submission_list, name='submission_list'),
    path('submission-list-new', views.submission_new_type_list,
         name='submission_new_list'),
    path('task-submission/<int:task_id>/',
         views.task_submission_form_view, name='task_submission'),
    path('task-submission-new/<int:task_id>/',
         views.task_submission_new_type_form_view, name='task_submission_new'),
]
