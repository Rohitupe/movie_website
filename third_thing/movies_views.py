
# this movie views.py


from django.http import HttpResponse
from .models import Hindi

# this is for showing name of the movie in link format

def index(request):
	all_movies=Hindi.objects.all()
	html=''
	for a in all_movies:
		url='/movie/'+str(a.id)
		html += '<a href="' +url+ '">' + a.name + '</a><br>'
	return HttpResponse(html)

# after clicking showing the id of the movie
def detail(request,movie_id):
	return HttpResponse("<h2>Details for movie_id:" +str(movie_id)+ "</h2>")
