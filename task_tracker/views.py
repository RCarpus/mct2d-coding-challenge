from django.shortcuts import render, get_object_or_404, redirect
from task_tracker.models import Task, TaskSubmission, TaskSubmissionNewType
from django.forms import forms
from django.shortcuts import redirect
from django import forms
from django.urls import reverse


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class TaskSubmissionForm(forms.ModelForm):
    class Meta:
        model = TaskSubmission
        fields = ['content']

    def __init__(self, *args, **kwargs):
        self.task = kwargs.pop('task', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        submission = super().save(commit=False)
        submission.task = self.task
        if commit:
            submission.save()
        return submission


class TaskSubmissionNewTypeForm(forms.ModelForm):
    class Meta:
        model = TaskSubmissionNewType
        fields = ['content']

    def __init__(self, *args, **kwargs):
        self.task = kwargs.pop('task', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        submission = super().save(commit=False)
        submission.task = self.task
        if commit:
            submission.save()
        return submission


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_tracker:task_list')
    else:
        form = TaskForm()
    return render(request, 'task_tracker/task_form.html', {'form': form})


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_tracker:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_tracker/task_form.html', {'form': form, 'task': task})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_tracker/task_list.html', {'tasks': tasks})


def submission_list(request):
    submissions = TaskSubmission.objects.all()
    return render(request, 'task_tracker/submission_list.html', {'submissions': submissions, 'submission_type': "default"})


def submission_new_type_list(request):
    submissions = TaskSubmissionNewType.objects.all()
    return render(request, 'task_tracker/submission_list.html', {'submissions': submissions, 'submission_type': "new type"})


def task_submission_form_view(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskSubmissionForm(request.POST, task=task)
        if form.is_valid():
            form.save()
            return redirect('task_tracker:task_list')
    else:
        form = TaskSubmissionForm(task=task)
    return render(request, 'task_tracker/task_submission_form.html', {'form': form, 'task': task, 'submission_type': "default"})


def task_submission_new_type_form_view(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskSubmissionNewTypeForm(request.POST, task=task)
        if form.is_valid():
            form.save()
            return redirect('task_tracker:task_list')
    else:
        form = TaskSubmissionNewTypeForm(task=task)
    return render(request, 'task_tracker/task_submission_form.html', {'form': form, 'task': task, 'submission_type': "new type"})
