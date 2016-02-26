from django.conf.urls import url
from photo.views import home

urlpatterns = [
    url(r'^$', home),
    url(r'boite/', home),
    url(r'mot/', home),
    url(r'diapo/', home),
    url(r'groupe/', home),
]
