
# this movie views.py

#django inbuild library
from django.views import generic
from .models import Hindi,Song

class IndexView(generic.ListView):
	template_name='movie/index.html'
	context_object_name='all_movies'
	def get_queryset(self):
		return Hindi.objects.all()

class DetailView(generic.DetailView):
	model=Hindi
	template_name='movie/detail.html'
	context_object_name='movie'
