from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

class Hindi(models.Model):
	name=models.CharField(max_length=250)
	actor=models.CharField(max_length=250)
	actress=models.CharField(max_length=1000)
 
	def get_absolute_url(self):
		return reverse('movie:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.name+'_'

class Song(models.Model):
	movie_name=models.ForeignKey(Hindi,on_delete=models.CASCADE)
	file_type=models.CharField(max_length=10)
	song_title=models.CharField(max_length=250)
	 

	def __str__(self):
		return self.song_title
