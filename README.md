# omdb-api

## Description

omdb-api allows you to get available episodes, ratings, comments and more on the series Game of Thrones

## Built with 
* Django Rest Framework
* Docker
* PostgreSQL
* Redis
* Amazon WS

## Getting Started

In order to use this app you will need to make sure that the following
dependencies are installed on your system:
  - Docker
  - Python

After successfully installation pull this repository to your machine, in terminal choose root project directory and with running docker execute commands:
```
docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py retrieve_episodes
```

If you encounted an error and you are using Windows you probably need to change end of line sequence to LF in ```app/entrypoint.sh``` file

### Folder structure

Here's a folder structure for project:

```
omdb-api                                 # Root directory
    ├── .github/workflows                # Folder for workflows
    │   └── main.yaml
    ├── app                              # Django root folder
    │   ├── base                         # Django settings
    │   │   ├── __init__.py
    │   │   ├── asgi.py
    │   │   ├── celery.py                # Celery config
    │   │   ├── settings.py
    │   │   ├── test_settings.py         # Django settings for pytest
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── comments                     # Comments app
    │   │   ├── migrations
    │   │   │   ├── __init__.py
    │   │   │   └── 0001_initial.py
    │   │   ├── __init__.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── permissions.py
    │   │   ├── serializers.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── series                        # Series app
    │   │   ├── management
    │   │   │   └── retrieve_episodes.py  # manage.py command for retrieving episodes
    │   │   ├── migrations
    │   │   │   ├── __init__.py
    │   │   │   └── 0001_initial.py
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── serializers.py
    │   │   ├── tasks.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── tests/users                    # Tests folder
    │   │   ├── conftest.py
    │   │   └── test_users.py
    │   ├── users                          # Users app
    │   │   ├── migrations
    │   │   │   ├── __init__.py
    │   │   │   └── 0001_initial.py
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── serializers.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── Dockerfile                      # Dockerfiles used in development and production
    │   ├── Dockerfile.prod
    │   ├── entrypoint.prod.sh              # Entrypoints
    │   ├── entrypoint.sh
    │   ├── manage.py
    │   ├── pytest.ini                      # Pytest config file
    │   └── requirements.txt                # Required dependencies
    ├── nginx                               # Nginx
    │   ├── Dockerfile
    │   └── nginx.conf
    ├── .dockerignore
    ├── .env.dev                            # Environment variables for development and production
    ├── .env.prod
    ├── .env.prod.db
    ├── .gitignore
    ├── docker-compose.prod.yml             # Docker compose
    └── docker-compose.yml

```
## Usage

* After you started app you can follow this link http://localhost:8000/api/episodes/ and you will see list all episodes of Game of Thrones
* Also you can filter episodes in many ways, just use the options button on the bottom of the page
* You can get comments by api/episodes/your-episode-id/comments/
