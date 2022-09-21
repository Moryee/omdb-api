from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework import generics
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import CustomUserSerializer


class CustomUserCreate(generics.CreateAPIView):
    user_model = get_user_model()
    queryset = user_model.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        queryset = self.user_model.objects.filter(username=self.request.user.username)
        if queryset.exists():
            raise exceptions.ValidationError('User already exists')
        serializer.save()


class CustomUserLogout(views.APIView):

    def post(self, request):
        refresh_token = RefreshToken(request.data.get('refresh_token', ''))
        if refresh_token:
            refresh_token.blacklist()

        return Response('Success', status=status.HTTP_200_OK)
