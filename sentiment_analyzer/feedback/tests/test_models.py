from django.test import TestCase

from ..models import Feedback


class FeedbackTest(TestCase):
    def setUp(self):
        self.feedback = Feedback()

    def test_save_feedback_should_have_data_in_each_defined_field(self):
        self.feedback.message = "I'm happy"
        self.feedback.actual_sentiment = 'positive'
        self.feedback.predicted_sentiment = 'negative'
        self.feedback.save()

        feedback = Feedback.objects.latest('id')

        self.assertEqual(feedback.message, "I'm happy")
        self.assertEqual(feedback.actual_sentiment, 'positive')
        self.assertEqual(feedback.predicted_sentiment, 'negative')

    def test_question_should_have_metric_choices(self):
        actual = self.feedback.SENTIMENT_CHOICES

        expected = (
            ('positive', 'Positive'),
            ('neutral', 'Neutral'),
            ('negative', 'Negative'),
        )
        self.assertEqual(actual, expected)
