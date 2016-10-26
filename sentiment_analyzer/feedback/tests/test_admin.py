from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Feedback


class FeedbackAdminTest(TestCase):
    def setUp(self):
        User.objects.create_superuser('admin', 'admin@pronto.com', 'admin')
        self.client.login(username='admin', password='admin')
        self.url = '/admin/feedback/feedback/'

    def test_access_feedback_admin(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_feedback_admin_should_show_selected_columns(self):
        Feedback.objects.create(
            message='It is hard to say',
            actual_sentiment='neutral',
            predicted_sentiment='neutral',
        )

        response = self.client.get(self.url)

        expected = '<div class="text"><a href="?o=1">Message</a></div>'
        self.assertContains(response, expected, status_code=200)

        expected = '<div class="text"><a href="?o=2">Actual sentiment' \
            '</a></div>'
        self.assertContains(response, expected, status_code=200)

        expected = '<div class="text"><a href="?o=3">Predicted sentiment' \
            '</a></div>'
        self.assertContains(response, expected, status_code=200)
