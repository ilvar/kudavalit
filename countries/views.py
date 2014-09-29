# coding=utf-8
import re
import decimal
from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView, DetailView

from countries.models import Country


class IndexView(ListView):
    model = Country
    template_name = 'index.html'

index = IndexView.as_view()


class CountryView(DetailView):
    model = Country
    template_name = 'country.html'

country = CountryView.as_view()


class HelpView(TemplateView):
    template_name = 'help.html'

help_page = HelpView.as_view()


class AddView(TemplateView):
    template_name = 'add.html'

add_page = AddView.as_view()


class UploadView(TemplateView):
    template_name = 'upload.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated() or not request.user.is_superuser:
            return redirect('index')

        return super(UploadView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        f = request.FILES['xls']

        import openpyxl
        wb = openpyxl.load_workbook(f)
        sheet = wb['Sheet1']

        for r in sheet.range('A4:AA56'):
            name = r[0].value
            if not any([c.value for c in r[1:]]):
                continue

            has_sea = r[13].value and not u'нет' in r[13].value.lower()
            has_mountains = r[12].value and not u'нет' in r[12].value.lower()

            def get_number(s):
                if not s:
                    return None

                if isinstance(s, int):
                    return s

                if isinstance(s, decimal.Decimal):
                    return s

                numbers = re.match('^(\-?\d+)', s)
                if numbers:
                    return numbers.groups()[0]
                else:
                    return None

            try:
                Country.objects.get(name=name)
            except Country.DoesNotExist:
                c = Country.objects.create(
                    name=r[0].value,
                    business=r[1].value or None,
                    investor=r[2].value or None,
                    pension=r[3].value or None,
                    visa_run=r[4].value or None,
                    specialist=r[5].value or None,
                    happiness=get_number(r[6].value),
                    prosperity=get_number(r[7].value),
                    medicine=get_number(r[8].value),
                    criminal=r[9].value or None,
                    summer=get_number(r[10].value),
                    winter=get_number(r[11].value),
                    mountains=has_mountains,
                    sea=has_sea,
                    rent=get_number(r[14].value),
                    language=r[15].value or None,
                    additional=r[16].value or None,
                )
                print 'Created', c

        return redirect('index')

upload = UploadView.as_view()