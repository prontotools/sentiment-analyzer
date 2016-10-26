from django.db import models


class Feedback(models.Model):
    SENTIMENT_CHOICES = (
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative'),
    )

    message = models.TextField(blank=True)
