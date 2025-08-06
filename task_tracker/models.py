from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TaskSubmission(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='submissions')
    submission_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        '''
        Mark the task as completed when a submission is made
        '''
        if not self.task.completed:
            self.task.completed = True
            self.task.save()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-submission_date']

    def __str__(self):
        return f"{self.task.title}"


class TaskSubmissionNewType(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='submissions_new_type')
    submission_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        '''
        Mark the task as completed when a submission is made
        '''
        if not self.task.completed:
            self.task.completed = True
            self.task.save()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-submission_date']

    def __str__(self):
        return f"{self.task.title}"
