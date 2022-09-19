from django.db import models


class Episode(models.Model):
    season = models.IntegerField(blank=False)
    title = models.CharField(max_length=100, blank=False, default='')
    released = models.DateField()
    episode = models.IntegerField(blank=False)
    rating = models.FloatField(blank=True, null=True)
