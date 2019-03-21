# this is movie models.py


from __future__ import unicode_literals
from django.db import models

class Hindi(models.Model):
	name=models.CharField(max_length=200)
	actor=models.CharField(max_length=250)
	actress=models.CharField(max_length=250)

class Song(models.Model):
	movie_name=models.ForeignKey(Hindi,on_delete=models.CASCADE)
	file_type=models.CharField(max_length=10)
	song_title=models.CharField(max_length=250)




# link app to database

#1) website folder
#2) setting.py
#3) installed apps(line 33)
#  (add below line)
# 'movie.apps.MovieConfig',   # type this at there



# to reflect database structure insert this command

# python3 manage.py makemigrations movie
# python3 manage.py migrate


# now go to admin.py
