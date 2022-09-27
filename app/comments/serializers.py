from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'episode', 'title', 'text_content', 'contains_spoilers', 'publish_date']
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
            'episode': {'read_only': True},
        }
