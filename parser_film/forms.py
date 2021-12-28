from . import models, forms
from . import parser




class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Anime', 'Anime'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]
def parser_date(self):
    if self.data['media_type'] == 'Anime':
        anime_data = parser.parser()
        for i in anime_data:
            models.Film.objects.create(**i)
    
# def parser_data(self):
#     if self.data['madia_type'] == 'Jutsu':
#         jutsu_data = parser.parser()
#         for i in jutsu_data:
#             models.Serial.objects.create(**i)

