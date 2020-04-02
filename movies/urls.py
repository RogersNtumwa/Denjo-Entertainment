from django.urls import path
from .views import index
from .views import (index,
                    moviedetails,
                    getactionmovies,
                    getadevmovies,
                    getcommovies,
                    gethormovies,
                    getlovmovies)


urlpatterns = [
    path('', index, name="home"),
    path('movies/Action/', getactionmovies, name="Action"),
    path('movies/Adventure/', getadevmovies, name="Adventure"),
    path('movies/Commed/', getcommovies, name="Commed"),
    path('movies/Horror/', gethormovies, name="Horror"),
    path('movies/Lovestory/', getlovmovies, name="Lovestory"),
    path('<slug:slug>/', moviedetails, name='movie_details'),
]
