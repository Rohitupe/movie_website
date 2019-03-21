# this is for website urls.py

from django.conf.urls import include,url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movie/',include('movie.urls')),
]
