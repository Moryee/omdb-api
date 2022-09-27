from django.urls import path, include
from rest_framework.routers import DefaultRouter
from series import views

router = DefaultRouter()
router.register(r'episodes', views.EpisodeViewSet, basename="episode")

urlpatterns = [
    path('', include(router.urls)),
]
