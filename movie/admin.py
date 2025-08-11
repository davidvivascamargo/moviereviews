from django.contrib import admin
from .models import Movie, Review

#from .models import News

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)