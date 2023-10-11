from django.db import models
from django.contrib.admin.models import LogEntry


class ActionHistory(LogEntry):
    class Meta:
        proxy = True
