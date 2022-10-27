from django.shortcuts import render, redirect
from .forms import Movieform
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == "POST":
        form = Movieform(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = Movieform()
    context = {
        'form' : form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    form = Movieform(instance=movie)
    context = {
        'movie': movie,
        'form' : form,
    }
    return render(request, 'movies/update.html', context)

def delete(request):

    context = {

    }
    return redirect(request, 'movies:index', context)