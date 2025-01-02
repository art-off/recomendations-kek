from django.conf import settings
from django.db import models
from django.utils import timezone


class Recomendation(models.Model):
    reason_text = models.TextField()
    recomendation_text = models.TextField()

    def __str__(self):
        return self.reason_text