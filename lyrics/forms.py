from django import forms
from .models import Artist, Lyrics, Translation

class AddArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']
        labels = {'name':''}

class AddLyricsForm(forms.ModelForm):
    class Meta:
        model = Lyrics
        fields = ['title', 'text']
        labels = {'title':'tytuł', 'text':''}

class AddTranslationForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = ['title', 'text']
        labels = {'title':'tytuł','text':''}
