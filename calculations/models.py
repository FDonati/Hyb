from django.db import models
from django.utils import timezone

# Create your models here.


class Job(models.Model):
    """
    Job model to store Celery jobs
    """
    name = models.CharField(max_length=255)
    """
       The name of the Celery job
    """
    status = models.CharField(max_length=255, null=True, blank=True)
    """
       The status of the Celery job
    """
    created = models.DateTimeField(default=timezone.now)
    """
           The date the Celery job was created
    """
    completed = models.DateTimeField(null=True, blank=True)
    """
            The date the Celery job was completed
    """
    celery_id = models.CharField(max_length=255, null=True, blank=True)
    """
            The unique identifier for retrieving the results of the job from Celery
    """

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.pk)
