from django.urls import path

from .views import (
    HomeView,

    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,

    TeamListView,
    TeamDetailView,
    TeamCreateView,
    TeamUpdateView,
    TeamDeleteView,

    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,

    TaskTypeListView,
    TaskTypeDetailView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
)

app_name = "tasks"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    # TASKS
    path("tasks/", TaskListView.as_view(), name="task-list"),

    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail",
    ),

    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),

    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),

    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),

    # TEAMS
    path(
        "teams/",
        TeamListView.as_view(),
        name="team-list",
    ),

    path(
        "teams/<int:pk>/",
        TeamDetailView.as_view(),
        name="team-detail",
    ),

    path(
        "teams/create/",
        TeamCreateView.as_view(),
        name="team-create",
    ),

    path(
        "teams/<int:pk>/update/",
        TeamUpdateView.as_view(),
        name="team-update",
    ),

    path(
        "teams/<int:pk>/delete/",
        TeamDeleteView.as_view(),
        name="team-delete",
    ),

    # WORKERS
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list",
    ),

    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail",
    ),

    path(
        "workers/create/",
        WorkerCreateView.as_view(),
        name="worker-create",
    ),

    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update",
    ),

    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),

    # TASK TYPES
    path(
        "task-types/",
        TaskTypeListView.as_view(),
        name="tasktype-list",
    ),

    path(
        "task-types/<int:pk>/",
        TaskTypeDetailView.as_view(),
        name="tasktype-detail",
    ),

    path(
        "task-types/create/",
        TaskTypeCreateView.as_view(),
        name="tasktype-create",
    ),

    path(
        "task-types/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="tasktype-update",
    ),

    path(
        "task-types/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="tasktype-delete",
    ),
]
