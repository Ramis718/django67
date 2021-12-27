from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView

from parser_film.models import Film
from django.views.generic import ListView
from . import models, forms, parser


class FilmView(ListView):
    template_name = 'film_index.html'


    def get_queryset(self):
        return models.Film.objects.all()


class ParserAnimeView(FormView):
    template_name = 'parser.html'
    form_class = forms.ParserForm
    success_url = '/anime/'


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse(self.success_url)
        else:
            return super(ParserAnimeView, self).post(request, *args, **kwargs)