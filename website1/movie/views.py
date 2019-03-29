
# this movie views.py


# for getting the error with wrong id
from django.http import Http404
from django.http import HttpResponse
# this is for html file
from django.shortcuts import render,get_object_or_404 # this is use to get the error by the system itself 'remove try and except' after this
from .models import Hindi

# this is for showing name of the movie in link format
def index(request):
	all_movies=Hindi.objects.all()	
	context={'all_movies':all_movies}
	return render (request,'movie/index.html',context)

# after clicking showing the id of the movie
def detail(request,movie_id):
	#try:
	movie=Hindi.objects.get(id=movie_id)
	#except Hindi.DoesNotExist:
		#raise Http404("movie not present")

	return render (request,'movie/detail.html',{'movie':movie})
