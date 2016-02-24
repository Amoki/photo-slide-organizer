from django.conf.urls import url
from photo.views import home

urlpatterns = [
    url(r'^$', home),
]
