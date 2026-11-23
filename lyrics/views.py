from django.shortcuts import render, redirect
from .models import Artist, Translation, Lyrics
from .forms import AddArtistForm, AddLyricsForm, AddTranslationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request,'lyrics/index.html')

def artists(request):
    artists = Artist.objects.order_by('name')
    context = {'artists':artists}
    return render(request, 'lyrics/artists.html', context)

def artist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    lyrics = artist.lyrics_set.order_by("title")
    context = {'artist':artist, 'lyrics':lyrics}
    return render(request, 'lyrics/artist.html', context)

def lyric(request, lyric_id):
    lyric = Lyrics.objects.get(id=lyric_id)
    translations = lyric.translation_set.order_by("-author") # podaj translations należące do lyric
    context = {'lyric':lyric, 'translations':translations}
    return render(request, 'lyrics/lyric.html', context)

@login_required
def translation(request, t_id):
    translation = Translation.objects.get(id=t_id)
    context = {'translation':translation}
    return render(request, 'lyrics/translation.html', context)

@login_required
def add_artist(request):
    if request.method != 'POST':
        form = AddArtistForm()
    else:
        form = AddArtistForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('lyrics:artists')

    context = {'form':form}
    return render(request, 'lyrics/add_artist.html', context)

@login_required
def add_lyrics(request, artist_id):

    artist = Artist.objects.get(id=artist_id)

    if request.method != 'POST':
        form = AddLyricsForm()
    else:
        form = AddLyricsForm(data=request.POST)
        if form.is_valid():
            new_lyrics = form.save(commit=False)
            new_lyrics.artist = artist
            new_lyrics.save()
            return redirect('lyrics:artist', artist_id = artist_id)

    context = {'artist':artist, 'form':form}
    return render(request, 'lyrics/add_lyrics.html', context)

@login_required
def edit_lyrics(request, lyric_id):

    if User.is_staff:
            raise Http404
    
    lyric = Lyrics.objects.get(id=lyric_id)
    artist = lyric.artist

    if request.method != 'POST':
        form = AddLyricsForm(instance=lyric)
    else:
        form = AddLyricsForm(instance=lyric, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('lyrics:lyric', lyric_id=lyric_id)

    context = {'lyric': lyric, 'artist':artist, 'form':form}
    return render(request, 'lyrics/edit_lyrics.html', context)

@login_required
def add_translation(request, lyric_id):
    
    lyric = Lyrics.objects.get(id=lyric_id)
    artist = lyric.artist 

    if request.method != 'POST':
        form = AddTranslationForm()
    else:
        form = AddTranslationForm(data=request.POST)
        if form.is_valid():
            new_t = form.save(commit=False)
            new_t.lyrics = lyric
            new_t.author = request.user
            new_t.save()
            return redirect('lyrics:lyric', lyric_id=lyric_id)

    context = {'lyric':lyric, 'artist':artist, 'form':form}
    return render(request, 'lyrics/add_translation.html', context)

@login_required
def edit_translation(request, translation_id):
    translation = Translation.objects.get(id=translation_id)

    if translation.author != request.user:
        raise Http404

    if request.method != 'POST':
        form = AddTranslationForm(instance=translation)
    else:
        form = AddTranslationForm(instance=translation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('lyrics:translation', t_id=translation_id)
        
    context = {'translation':translation, 'form':form}
    return render(request, 'lyrics/edit_translation.html', context)