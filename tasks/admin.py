from django.contrib import admin

from .models import (
    Team,
    Worker,
    Task,
    TaskType,
)


admin.site.register(Team)
admin.site.register(Worker)
admin.site.register(Task)
admin.site.register(TaskType)
