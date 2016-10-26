from django.test import TestCase

from ..models import Feedback


class FeedbackTest(TestCase):
    def test_save_feedback_should_have_data_in_each_defined_field(self):
        feedback = Feedback()
        feedback.message = "I'm happy"
        feedback.save()

        feedback = Feedback.objects.latest('id')

        expected = "I'm happy"
        self.assertEqual(feedback.message, expected)
