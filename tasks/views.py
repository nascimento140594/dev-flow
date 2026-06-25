from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Task, Team, Worker, TaskType


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "tasks/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["num_tasks"] = Task.objects.count()
        context["num_teams"] = Team.objects.count()
        context["num_workers"] = Worker.objects.count()
        context["num_task_types"] = TaskType.objects.count()

        return context


# TASK CRUD

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        worker = Worker.objects.filter(
            user=self.request.user
        ).first()

        if not worker:
            return Task.objects.none()

        return Task.objects.filter(
            assignees=worker
        ).distinct()


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = "__all__"
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:task-list")


# TEAM CRUD

class TeamListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = "tasks/team_list.html"
    context_object_name = "teams"


class TeamDetailView(LoginRequiredMixin, DetailView):
    model = Team
    template_name = "tasks/team_detail.html"
    context_object_name = "team"


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    fields = "__all__"
    template_name = "tasks/team_form.html"
    success_url = reverse_lazy("tasks:team-list")


class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    fields = "__all__"
    template_name = "tasks/team_form.html"
    success_url = reverse_lazy("tasks:team-list")


class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = Team
    template_name = "tasks/team_confirm_delete.html"
    success_url = reverse_lazy("tasks:team-list")


# WORKER CRUD

class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    template_name = "tasks/worker_list.html"
    context_object_name = "workers"


class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker
    template_name = "tasks/worker_detail.html"
    context_object_name = "worker"


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = Worker
    fields = "__all__"
    template_name = "tasks/worker_form.html"
    success_url = reverse_lazy("tasks:worker-list")


class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    model = Worker
    fields = "__all__"
    template_name = "tasks/worker_form.html"
    success_url = reverse_lazy("tasks:worker-list")


class WorkerDeleteView(LoginRequiredMixin, DeleteView):
    model = Worker
    template_name = "tasks/worker_confirm_delete.html"
    success_url = reverse_lazy("tasks:worker-list")


# TASK TYPE CRUD

class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    template_name = "tasks/tasktype_list.html"
    context_object_name = "task_types"


class TaskTypeDetailView(LoginRequiredMixin, DetailView):
    model = TaskType
    template_name = "tasks/tasktype_detail.html"
    context_object_name = "task_type"


class TaskTypeCreateView(LoginRequiredMixin, CreateView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/tasktype_form.html"
    success_url = reverse_lazy("tasks:tasktype-list")


class TaskTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/tasktype_form.html"
    success_url = reverse_lazy("tasks:tasktype-list")


class TaskTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskType
    template_name = "tasks/tasktype_confirm_delete.html"
    success_url = reverse_lazy("tasks:tasktype-list")
