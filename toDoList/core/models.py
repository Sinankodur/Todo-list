from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    PENDING = 'pending'
    COMPLETED = 'completed'

    STATUS_CHOICES = (
        (COMPLETED, 'Completed'),
        (PENDING, 'Pending')
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    class Meta:
        verbose_name_plural = 'Tasks'
        ordering = ('created_at',)

    def __str__(self):
        return self.name