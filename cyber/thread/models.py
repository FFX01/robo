from django.db import models

from board.models import Board


class Thread(models.Model):
    title = models.CharField(
        verbose_name='Title',
        blank=True,
        max_length=120,
    )
    timestamp = models.DateTimeField(
        verbose_name='Timestamp',
        blank=True,
        auto_now_add=True,
    )
    board = models.ForeignKey(
        Board,
        blank=False,
        null=False,
        related_name='threads'
    )

    def get_posts(self):
        return self.posts.objects.all()

    def get_post_count(self):
        return self.posts.all().count()

    class Meta:
        verbose_name = 'Thread'
        verbose_name_plural = 'Threads'
        get_latest_by = 'id'

    def __str__(self):
        return "%d - %s" % (self.id, self.title)
