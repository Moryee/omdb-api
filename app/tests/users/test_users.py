import pytest
from rest_framework_simplejwt.tokens import BlacklistedToken


@pytest.mark.django_db
def test_register_user(client, test_user_data):
    response = client.post('/users/registration/', test_user_data)

    data = response.data

    assert response.status_code == 201
    assert data['username'] == test_user_data['username']
    assert data['email'] == test_user_data['email']
    assert 'password' not in data


@pytest.mark.django_db
def test_login_user(client, test_user_data, register_user):
    user = register_user()

    response = client.post('/api/token/', dict(email=user['email'], password=test_user_data['password']))

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail(client):
    response = client.post('/api/token/', dict(email='fail@gmail.com', password='qwerty'))

    assert response.status_code == 401


@pytest.mark.django_db
def test_logout_user(client, auto_login_user):
    data = auto_login_user()

    response = client.post('/users/logout/', dict(token=data['access'], refresh_token=data['refresh']))

    assert response.status_code == 200


@pytest.mark.django_db
def test_verify_token(client, auto_login_user):
    token = auto_login_user()['access']

    response = client.post('/api/token/verify/', dict(token=token))

    assert response.status_code == 200


@pytest.mark.django_db
def test_refresh_token(client, auto_login_user):
    data = auto_login_user()

    response = client.post('/api/token/refresh/', dict(token=data['access'], refresh=data['refresh']))

    assert response.status_code == 200

    response = client.post('/api/token/verify/', dict(token=response.data['access']))

    assert response.status_code == 200


@pytest.mark.django_db
def test_blacklist_token(client, auto_login_user):
    data = auto_login_user()

    response = client.post('/users/logout/', dict(token=data['access'], refresh_token=data['refresh']))

    assert response.status_code == 200
    assert BlacklistedToken.objects.count() == 1
