from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from thread.models import Thread


class Post(MPTTModel):
    timestamp = models.DateTimeField(
        verbose_name='Timestamp',
        auto_now_add=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name='Image',
        upload_to='img/%Y/%m/%d',
        blank=True,
    )
    body = models.TextField(
        verbose_name='Comment',
        blank=False,
    )
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
    )
    parent_thread = models.ForeignKey(
        Thread,
        related_name='posts',
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        get_latest_by = 'id'

    def __str__(self):
        return str(self.id)
