from task_tracker.models import Task
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seed the database with initial tasks'

    def handle(self, *args, **kwargs):
        tasks = [
            {
                'title': 'Task 1',
                'description': 'Description for Task 1',
                'due_date': '2023-10-01T12:00:00Z',
                'completed': False,
            },
            {
                'title': 'Task 2',
                'description': 'Description for Task 2',
                'due_date': '2023-10-02T12:00:00Z',
                'completed': False,
            },
            {
                'title': 'Task 3',
                'description': 'Description for Task 3',
                'due_date': None,
                'completed': True,
            },
        ]

        for task_data in tasks:
            task, created = Task.objects.get_or_create(**task_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created task: {task.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Task already exists: {task.title}'))