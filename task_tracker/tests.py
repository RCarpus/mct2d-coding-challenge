from django.test import TestCase, Client
from django.urls import reverse
from task_tracker.models import Task, TaskSubmission, TaskSubmissionNewType


class TaskTrackerTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            due_date="2030-01-01T12:00"
        )

    def test_create_task(self):
        response = self.client.post(reverse('task_tracker:add_task'), {
            'title': 'New Task',
            'description': 'New Task Description',
            'due_date': '2030-01-01T12:00'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_update_task(self):
        response = self.client.post(reverse('task_tracker:update_task', args=[self.task.id]), {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'due_date': '2030-01-01T12:00'
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_delete_task(self):
        response = self.client.post(
            reverse('task_tracker:delete_task', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_task_list(self):
        response = self.client.get(reverse('task_tracker:task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.title)

    def test_task_submission_default(self):
        response = self.client.post(reverse('task_tracker:task_submission', args=[self.task.id]), {
            'content': 'Submission content'
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)
        self.assertTrue(TaskSubmission.objects.filter(task=self.task).exists())

    def test_task_submission_new_type(self):
        task = Task.objects.create(
            title="New Type Task",
            description="Submission type 2",
            due_date="2030-01-01T12:00"
        )
        response = self.client.post(reverse('task_tracker:task_submission_new', args=[task.id]), {
            'content': 'New type submission'
        })
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertTrue(task.completed)
        self.assertTrue(
            TaskSubmissionNewType.objects.filter(task=task).exists())
