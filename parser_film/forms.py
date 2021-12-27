from django import forms
from . import models
from . import parser




class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('film', 'film'),
    )
    media_type = forms.CharField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]
def parser_date(self):
    if self.data['media_type'] == 'film':
        anime_data = parser.parser()
        for i in anime_data:
            models.Film.objects.create(**i)
    elif self.data['media_type'] == 'film'       

