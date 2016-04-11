from django.conf.urls import url
from photo.views import home, search

urlpatterns = [
    url(r'^$', home),
    url(r'boite/', home),
    url(r'diapo/', home),
    url(r'search/', search),
]
