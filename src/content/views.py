from django.conf import settings
from django.views.generic import TemplateView

from butter_cms import ButterCMS

butter_client = ButterCMS(settings.BUTTER_CMS.get('KEY'))


class ContentView(TemplateView):
    client = butter_client
    butter_type = None

    def get_template_names(self):
        return 'butter/{}.html'.format(self.butter_type)

    def render_to_response(self, context, **response_kwargs):
        butter = self.client.pages.get(self.butter_type, self.kwargs.get('slug'))
        context['object'] = butter.get('data', {}).get('fields', {})
        return super(ContentView, self).render_to_response(context, **response_kwargs)