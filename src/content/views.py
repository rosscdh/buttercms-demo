from django.http import Http404
from django.conf import settings
from django.views.generic import TemplateView

from butter_cms import ButterCMS

butter_client = ButterCMS(settings.BUTTER_CMS.get('KEY'))


class ContentView(TemplateView):
    client = butter_client
    butter_type = None

    def get_template_names(self):
        templates = ['butter/{}.html'.format(self.butter_type)]
        if self.template_name:
            templates.insert(0, self.template_name)
        return templates

    def render_to_response(self, context, **response_kwargs):
        butter = self.client.pages.get(self.butter_type, self.kwargs.get('slug'))

        if 'page not found' in butter.get('detail', '').lower():
            raise Http404("An error occurred: {}".format(butter))

        try:
            context['object'] = butter.get('data', {}).get('fields', {})
        except Exception as e:
            raise Http404("An error occurred: {}".format(butter))

        return super(ContentView, self).render_to_response(context, **response_kwargs)