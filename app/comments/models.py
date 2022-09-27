from django.db import models
from django.contrib.auth import get_user_model
from series.models import Episode


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=50)
    text_content = models.TextField()
    contains_spoilers = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True)
