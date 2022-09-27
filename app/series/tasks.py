from os import environ
from celery import shared_task
from series.models import Episode
from parse import parse

import requests
import datetime


@shared_task
def retrieve_episodes():
    key = 'a46d1bf5'
    episodes = []

    total_seasons = int(
        requests.get(f'http://www.omdbapi.com/?t=Game+Of+Thrones&apikey={key}')
        .json()['totalSeasons']
    )

    count_episodes_last_season = len(
        requests.get(f'http://www.omdbapi.com/?t=Game+Of+Thrones&season={total_seasons}&apikey={key}')
        .json()['Episodes']
    )

    if Episode.objects.filter(season=total_seasons).count() == count_episodes_last_season:  # ??
        return 'Database already up to date'

    for i in range(total_seasons):
        raw_ep_list = requests.get(f'http://www.omdbapi.com/?t=Game+Of+Thrones&season={i + 1}&apikey={key}').json()['Episodes']

        for ep in raw_ep_list:
            date = parse('{y:d}-{m:d}-{d:d}', ep['Released'])

            episodes.append(Episode(
                title=ep['Title'],
                season=i + 1,
                released=datetime.date(date['y'], date['m'], date['d']),
                episode=int(ep['Episode']),
                rating=float(ep['imdbRating']) if not ep['imdbRating'] == 'N/A' else None
            ))

    Episode.objects.all().delete()
    Episode.objects.bulk_create(episodes)
    return 'Database updated'
