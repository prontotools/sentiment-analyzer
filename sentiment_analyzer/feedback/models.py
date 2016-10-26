from django.db import models


class Feedback(models.Model):
    message = models.TextField(blank=True)
