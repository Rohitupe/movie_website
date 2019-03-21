# this is movie urls.py


from django.conf.urls import url
from . import views

urlpatterns=[
 	#/music/
	url(r'^$',views.index,name='index'),
	
	#/music/712/

	# this is for showing the id from 0 to 9
	url(r'^(?P<movie_id>[0-9]+)$',views.detail,name='detail'),

]
