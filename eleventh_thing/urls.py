# this is movie urls.py


from django.conf.urls import url
from . import views
app_name='movie'
urlpatterns=[
 	#/music/
	url(r'^$',views.IndexView.as_view(),name='index'),
	
	#/music/712/

	# this is for showing the id from 0 to 9
	url(r'^(?P<pk>[0-9]+)$',views.DetailView.as_view(),name='detail'),

]
