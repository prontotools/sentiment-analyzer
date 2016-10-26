from django.db import models


class Feedback(models.Model):
    SENTIMENT_CHOICES = (
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative'),
    )

    message = models.TextField(blank=True)
    actual_sentiment = models.CharField(
        null=False,
        blank=False,
        max_length=8,
        choices=SENTIMENT_CHOICES,
        default='neutral'
    )
    predicted_sentiment = models.CharField(
        null=False,
        blank=False,
        max_length=8,
        choices=SENTIMENT_CHOICES,
        default='neutral'
    )
