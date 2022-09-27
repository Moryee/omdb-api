from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets

from comments.permissions import IsAuthorOrAdmin
from comments.serializers import CommentSerializer
from series.models import Episode


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        instance = Episode.objects.filter(id=self.kwargs.get('episode_id', 1)).prefetch_related('comments').get()
        return instance.comments.select_related('episode').select_related('user')

    def get_permissions(self):
        permission_classes = (permissions.AllowAny, )
        if self.action == 'create':
            permission_classes = (permissions.IsAuthenticated, )
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = (permissions.IsAuthenticated, IsAuthorOrAdmin)

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        episode_obj = get_object_or_404(Episode, pk=self.kwargs.get('episode_id', 1))
        serializer.save(user=self.request.user, episode=episode_obj)
