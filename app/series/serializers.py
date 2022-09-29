from rest_framework import serializers
from rest_framework.reverse import reverse
from series.models import Episode
from comments.models import Comment


class CommentsHyperlink(serializers.HyperlinkedRelatedField):
    view_name = 'comment-list'
    queryset = Comment.objects.all()

    def get_url(self, obj, view_name, request, format):
        try:
            episode_id = obj.all().first().episode.id
        except AttributeError:
            return

        url_kwargs = {
            'episode_id': episode_id,
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'episode_id': view_kwargs['episode_id'],
        }
        return self.get_queryset().get(**lookup_kwargs)


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentsHyperlink()

    class Meta:
        model = Episode
        fields = ['id', 'season', 'episode', 'title', 'released', 'rating', 'comments']
        extra_kwargs = {
            'id': {'read_only': True},
        }
