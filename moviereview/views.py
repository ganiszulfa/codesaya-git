from django.shortcuts import render
from django.http import HttpResponse
from .models import movieinfo
# Create your views here.
def index(request):
    return render(request, "moviereview/header2.html")


def addmovie(request):
    return render(request, "moviereview/add_movie.html")

def addmoviesuccess(request) :
    print("Submitted")
    movie_name = request.POST["movie_name"]
    movie_type = request.POST["movie_type"]
    movie_review = request.POST["movie_review"]
    movie_release_date = request.POST["movie_release_date"]
    movie_detail = request.POST["movie_detail"]
    movie_info = movieinfo(movie_name=movie_name,movie_type=movie_type,movie_review=movie_review,movie_release_date=movie_release_date,movie_detail=movie_detail)
    movie_info.save()
    return render(request,"moviereview/add_movie.html")