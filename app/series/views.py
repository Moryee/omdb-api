from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter

from series.models import Episode
from series.serializers import EpisodeSerializer
from series.tasks import retrieve_episodes


class EpisodeFilter(FilterSet):
    min_rating = NumberFilter(field_name='rating', lookup_expr='gte')
    max_rating = NumberFilter(field_name='rating', lookup_expr='lte')

    class Meta:
        model = Episode
        fields = ['rating', 'season']


class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_class = EpisodeFilter
    search_fields = ['title']
    ordering_filter = '__all__'
