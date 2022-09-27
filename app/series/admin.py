from django.contrib import admin
from series.models import Episode


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ('season', 'title', 'release', 'episode', 'rating')
