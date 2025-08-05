from django.contrib import admin
from task_tracker.models import Task, TaskSubmission
from django.utils.html import format_html
from django.urls import reverse


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at', 'due_date', 'completed')
    search_fields = ('title', 'description')
    list_filter = ('completed',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 10


@admin.register(TaskSubmission)
class TaskSubmissionAdmin(admin.ModelAdmin):
    list_display = ('task_link', 'submission_date', 'content')
    search_fields = ('task__title', 'content')
    ordering = ('-submission_date',)
    date_hierarchy = 'submission_date'
    list_per_page = 10

    def task_link(self, obj):
        url = reverse('admin:task_tracker_task_change', args=[obj.task.id])
        return format_html('<a href="{}">{}</a>', url, obj.task.title)

    task_link.short_description = 'Task'
