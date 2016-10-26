from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import Feedback


class FeedbackViewTest(TestCase):
    def setUp(self):
        self.url = reverse('feedback')

    def test_access_feedback_index_page(self):
        response = self.client.get(self.url)

        expected = '<h1>Feedback</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_feedback_page_should_have_feedback_table(self):
        response = self.client.get(self.url)

        expected = '<th>Message</th>'
        expected += '<th>Actual</th>'
        expected += '<th>Predicted</th>'
        self.assertContains(response, expected, status_code=200)

    def test_feedback_page_should_show_feedback_data(self):
        message = 'I wanna talk to someone or explain on some requests. ' \
            'Not just only write down what I want you to do.'
        Feedback.objects.create(
            message=message,
            actual_sentiment='positive',
            predicted_sentiment='neutral'
        )

        response = self.client.get(self.url)

        expected = '<td>' + message + '</td>'
        expected += '<td><img src="/static/img/feedback_positive.png" /></td>'
        expected += '<td><img src="/static/img/feedback_neutral.png" /></td>'
        self.assertContains(response, expected, status_code=200)

    def test_feedback_page_should_show_dashes_if_no_sentiment_set(self):
        message = 'I wanna talk to someone or explain on some requests. ' \
            'Not just only write down what I want you to do.'
        Feedback.objects.create(
            message=message
        )

        response = self.client.get(self.url)

        expected = '<td>' + message + '</td>'
        expected += '<td>---</td>'
        expected += '<td>---</td>'
        self.assertContains(response, expected, status_code=200)
