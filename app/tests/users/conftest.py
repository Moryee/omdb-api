import pytest

user_data = dict(
    email='harry@gmail.com',
    username='Harry',
    password='qwerty1234qwerty'
)


@pytest.fixture
def test_user_data():
    return user_data


@pytest.fixture
def register_user(client):
    def make_user(**kwargs):
        if 'email' not in kwargs:
            kwargs['email'] = user_data['email']
        if 'username' not in kwargs:
            kwargs['username'] = user_data['username']
        kwargs['password'] = user_data['password']
        return client.post('/users/registration/', user_data).data
    return make_user


@pytest.fixture
def auto_login_user(client, register_user):
    def make_auto_login(user=None):
        if user is None:
            user = register_user()
        return client.post('/api/token/', dict(email=user['email'], password=user_data['password'])).data
    return make_auto_login
