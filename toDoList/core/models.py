from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Tasks'
        ordering = ('created_at',)

    def __str__(self):
        return self.name