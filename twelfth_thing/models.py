# this is movie models.py


from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

class Hindi(models.Model):
	name=models.CharField(max_length=200)
	actor=models.CharField(max_length=250)
	actress=models.CharField(max_length=250)

	def get_absolute_url(self):
		return reverse('movie:detail', kwargs={'pk':self.pk})

# this for showing the name of the movie

	def __str__ (self):
		return self.name + '_'

class Song(models.Model):
	movie_name=models.ForeignKey(Hindi,on_delete=models.CASCADE)
	file_type=models.CharField(max_length=10)
	song_title=models.CharField(max_length=250)

# this for showing the title of the particular song for the movie
	def __str__ (self):
		return self.song_title
