from django.db import models
from django.core.urlresolvers import reverse
import datetime


class Board(models.Model):
    timestamp = models.DateTimeField(
        blank=True,
        auto_now_add=True,
    )
    name = models.CharField(
        verbose_name='Board Name',
        blank=False,
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name='URL Slug',
        blank=False,
        max_length=10,
    )
    info = models.TextField(
        verbose_name='Board info and rules',
        blank=True,
    )

    def get_threads(self):
        current_date = datetime.datetime.today()
        delta = datetime.timedelta(days=30)
        oldest = current_date - delta
        return self.threads.all().filter(timestamp >= oldest)

    def get_absolute_url(self):
        return reverse(
            'board:single_board',
            kwargs={'slug': self.slug},
        )

    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'
        get_latest_by = 'id'

    def __str__(self):
        return self.name
