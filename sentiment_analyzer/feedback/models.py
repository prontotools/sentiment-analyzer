from django.db import models


class Feedback(models.Model):
    SENTIMENT_CHOICES = (
        ('', '---'),
        ('positive', 'positive'),
        ('neutral', 'neutral'),
        ('negative', 'negative'),
    )

    message = models.TextField(blank=True)
    actual_sentiment = models.CharField(
        null=True,
        blank=True,
        max_length=8,
        choices=SENTIMENT_CHOICES,
        default=''
    )
    predicted_sentiment = models.CharField(
        null=True,
        blank=True,
        max_length=8,
        choices=SENTIMENT_CHOICES,
        default=''
    )
