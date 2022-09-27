from django.contrib import admin
from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ('episode', 'title', 'text_content', 'publish_date')
