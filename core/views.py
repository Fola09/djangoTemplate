from django.contrib.auth.views import TemplateView


# Create your views here.
class HompePageView(TemplateView):
    template_name = 'homepage.html'

    # form = EmailSignupForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # scontext['form'] = self.form
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    # form = EmailSignupForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'] = self.form
        return context
