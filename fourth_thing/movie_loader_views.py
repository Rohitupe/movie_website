
# this movie views.py


from django.http import HttpResponse
# this is for html file
from django.template import loader
from .models import Hindi

# this is for showing name of the movie in link format
def index(request):
	all_movies=Hindi.objects.all()
	template=loader.get_template('movie/index.html')	
	context={'all_movies':all_movies}
	return HttpResponse (template.render(context,request))

# after clicking showing the id of the movie
def detail(request,movie_id):
	return HttpResponse("<h2>Details for movie_id:" +str(movie_id)+ "</h2>")
