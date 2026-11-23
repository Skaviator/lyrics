from django.contrib import admin
from .models import Artist, Lyrics, Translation

# Register your models here.
admin.site.register(Artist)
admin.site.register(Lyrics)
admin.site.register(Translation)