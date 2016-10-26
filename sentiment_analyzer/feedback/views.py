from django.shortcuts import render

from django.views.generic import TemplateView


class FeedbackView(TemplateView):
    template_name = 'feedback.html'

    def get(self, request):
        return render(request, self.template_name)
