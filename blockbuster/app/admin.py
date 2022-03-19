from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class MovieForm(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'get_photo')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    save_on_top = True
    prepopulated_fields = {'slug': ('name',)}
    fields = (
        'name', 'slug', 'genre', 'year', 'release_date', 'run_time', 'director', 'actors', 'media', 'photo', 'get_photo',
        'description', 'created_at', 'trailer')
    readonly_fields = ('get_photo', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


class CelebrityForm(admin.ModelAdmin):
    list_display = ('id', 'name', 'profession', 'get_photo', 'date_of_birth',)
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    save_on_top = True
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'profession', 'country', 'description', 'media', 'filmography', 'photo', 'get_photo', 'date_of_birth', 'biography',)
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


class GenreForm(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class MediaForm(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_photo')
    fields = ('name', 'photo', 'get_photo')
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'

class ReviewsForm(admin.ModelAdmin):
    list_display = ('id', 'name', 'movie', 'created_at')
    readonly_fields = ('created_at',)


admin.site.register(Movie, MovieForm)
admin.site.register(Celebrity, CelebrityForm)
admin.site.register(Media, MediaForm)
admin.site.register(Genre, GenreForm)
admin.site.register(Profession)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews, ReviewsForm)
