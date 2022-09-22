from django.urls import path

from users import views


urlpatterns = [
    path('registration/', views.CustomUserCreate.as_view(), name='custom_user_registration'),
    path('logout/', views.CustomUserLogout.as_view(), name='custom_user_logout')

]
