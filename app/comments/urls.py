from django.urls import path, include
from rest_framework.routers import DefaultRouter

from comments import views

router = DefaultRouter()
router.register(
    r'(?P<episode_id>\d+)/comments',
    views.CommentViewSet,
    basename="comment"
)


urlpatterns = [
    path('', include(router.urls)),
]
