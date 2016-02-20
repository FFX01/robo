from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^(?P<id>[0-9]+)/$',
        views.SingleThread.as_view(),
        name='single_thread',
    ),
]
