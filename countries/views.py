from django.views.generic import ListView, TemplateView

from countries.models import Country


class IndexView(ListView):
    model = Country
    template_name = 'index.html'

index = IndexView.as_view()


class HelpView(TemplateView):
    template_name = 'help.html'

help_page = HelpView.as_view()


class AddView(TemplateView):
    template_name = 'add.html'

add_page = AddView.as_view()


class UploadView(TemplateView):
    template_name = 'upload.html'

upload = UploadView.as_view()