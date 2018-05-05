from django.http import Http404
from django.conf import settings
from django.views.generic import TemplateView

from butter_cms import ButterCMS

butter_client = ButterCMS(settings.BUTTER_CMS.get('KEY'))


class ButterPageDetailView(TemplateView):
    client = butter_client
    butter_type = 'pages'

    def get_template_names(self):
        templates = ['butter/{}_detail.html'.format(self.butter_type)]
        if self.template_name:
            templates.insert(0, self.template_name)
        return templates

    def get_butter(self):
        return self.client.pages.get(self.butter_type, self.kwargs.get('slug'))

    def render_to_response(self, context, **response_kwargs):
        butter = self.get_butter()

        if 'page not found' in butter.get('detail', '').lower():
            raise Http404("An error occurred: {}".format(butter))

        try:
            context['object'] = butter.get('data', {}).get('fields', {})
        except Exception as e:
            raise Http404("An error occurred: {}".format(butter))

        return super(ButterPageDetailView, self).render_to_response(context, **response_kwargs)


class ButterBlogDetailView(ButterPageDetailView):
    butter_type = 'posts'

    def get_butter(self):
        return getattr(self.client, self.butter_type).get(self.kwargs.get('slug'))


class ButterGenericListView(TemplateView):
    client = butter_client
    butter_type = 'posts'

    def get_template_names(self):
        templates = ['butter/{}_list.html'.format(self.butter_type)]
        if self.template_name:
            templates.insert(0, self.template_name)
        return templates

    def render_to_response(self, context, **response_kwargs):
        butter = getattr(self.client, self.butter_type).all()

        if 'page not found' in butter.get('detail', '').lower():
            raise Http404("An error occurred: {}".format(butter))

        try:
            context['object_list'] = butter.get('data', {}).get('fields', {})
        except Exception as e:
            raise Http404("An error occurred: {}".format(butter))

        return super(ButterGenericListView, self).render_to_response(context, **response_kwargs)


class ButterPageListView(ButterGenericListView):
    butter_type = 'pages'


class ButterBlogListView(ButterGenericListView):
    butter_type = 'posts'

