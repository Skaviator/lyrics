from django.urls import path
from . import views

app_name = 'lyrics'
urlpatterns = [
    path('', views.index, name='index'),
    path('artists', views.artists, name='artists'),
    path('artist/<int:artist_id>', views.artist, name='artist'),
    path('lyric/<int:lyric_id>', views.lyric, name='lyric'),
    path('translation/<int:t_id>', views.translation, name='translation'),
    path('add_artist', views.add_artist, name='add_artist'),
    path('add_lyrics/<int:artist_id>',views.add_lyrics, name='add_lyrics'),
    path('edit_lyrics/<int:lyric_id>', views.edit_lyrics, name='edit_lyrics'),
    path('add_translation/<int:lyric_id>', views.add_translation, name='add_translation'),
    path('edit_translation/<int:translation_id>', views.edit_translation, name='edit_translation')
]
