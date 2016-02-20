from django.contrib import admin

from . import models


@admin.register(models.Thread)
class ThreadAdmin(admin.ModelAdmin):
    pass
