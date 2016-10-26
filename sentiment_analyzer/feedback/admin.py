from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'message',
        'actual_sentiment',
        'predicted_sentiment',
    )
