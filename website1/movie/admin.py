# this is movie admin.py


from django.contrib import admin
from .models import Hindi,Song


admin.site.register(Hindi)
admin.site.register(Song)
