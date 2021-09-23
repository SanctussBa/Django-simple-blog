from django.contrib import admin
from .models import Article #get the models file in the current directory

admin.site.register(Article) # we are telling to Django to register Article module on the admin site
