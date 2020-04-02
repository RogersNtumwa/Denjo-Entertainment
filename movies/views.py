from django.shortcuts import render, get_object_or_404
from .models import movie
from .forms import moviesForm
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def index(request):
    allmovies = movie.objects.all().order_by('year_published').reverse()
    query = request.GET.get("search")
    if query:
        allmovies = allmovies.filter(
            Q(title__icontains=query) | Q(genre__icontains=query))

    paginator = Paginator(allmovies, 12)

    page = request.GET.get("page")
    allmovies = paginator.get_page(page)
    context = {
        'allmovies': allmovies,
    }
    return render(request, 'movies/index.html', context)


@login_required
def moviedetails(request, slug):
    clip = get_object_or_404(movie, slug=slug)

    similar_movies = movie.objects.filter(
        genre=clip.genre).exclude(title=clip.title)

    paginator = Paginator(similar_movies, 6)

    page = request.GET.get("page")
    similar_movies = paginator.get_page(page)

    context = {
        'clip': clip,
        'similar_movies': similar_movies,
    }
    return render(request, 'movies/movieDetail.html', context)


def getactionmovies(request):  # to be continued
    allmovies = movie.objects.filter(
        genre="Action").order_by("year_published").reverse()

    paginator = Paginator(allmovies, 2)

    page = request.GET.get("page")
    allmovies = paginator.get_page(page)

    context = {
        "allmovies": allmovies,
    }
    return render(request, 'movies/index.html', context)


def getadevmovies(request):  # to be continued
    allmovies = movies.objects.filter(
        genre="Adventure").order_by("year_published").reverse()

    paginator = Paginator(allmovies, 2)

    page = request.GET.get("page")
    allmovies = paginator.get_page(page)
    context = {
        "allmovies": allmovies,
    }
    return render(request, 'movies/index.html', context)


def gethormovies(request):  # to be continued
    allmovies = movie.objects.filter(
        genre="Horror").order_by("year_published").reverse()
    context = {
        "allmovies": allmovies,
    }
    return render(request, 'movies/index.html', context)


def getcommovies(request):  # to be continued
    allmovies = movie.objects.filter(
        genre="Commed").order_by("year_published").reverse()
    context = {
        "allmovies": allmovies,
    }
    return render(request, 'movies/index.html', context)


def getlovmovies(request):  # to be continued
    allmovies = movie.objects.filter(
        genre="LoveStory").order_by("year_published").reverse()
    context = {
        "allmovies": allmovies,
    }
    return render(request, 'movies/index.html', context)
