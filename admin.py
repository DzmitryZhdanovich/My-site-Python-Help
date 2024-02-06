from django.contrib import admin

# Register your models here.
# Author, Post - наши классы в models.py.
from .models import Author, Post

admin.site.register(Author)
admin.site.register(Post)