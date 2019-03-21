# this movie views.py


from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>This is movie website</h1>")
