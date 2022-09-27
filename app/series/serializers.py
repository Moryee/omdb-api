from rest_framework import serializers
from series.models import Episode


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['id', 'season', 'episode', 'title', 'released', 'rating']
        extra_kwargs = {
            'id': {'read_only': True},
        }
