from django.conf.urls import url

from .views import SingleBoard


urlpatterns = [
    url(
        r'(?P<slug>[a-zA-Z0-9\-]+)/$',
        SingleBoard.as_view(),
        name='single_board',
    ),
]
