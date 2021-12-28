from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from parser_film.models import Film
from django.views.generic import ListView
from . import models, forms, parser
import requests
from django.http.response import HttpResponseRedirect


class AnimeView(ListView):
    model = models.Film
    template_name = 'anime.list.html'


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
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ParserAnimeView, self).post(request, *args, **kwargs)