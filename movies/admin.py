from django.contrib import admin
from .models import movie


class moviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_published', 'genre')
    list_filter = ('genre', 'year_published')
    search_fields = ('title', 'genre')
    list_display_links = ('title',)
    list_per_page = 25


admin.site.register(movie, moviesAdmin)
