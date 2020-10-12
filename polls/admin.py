from django.contrib import admin
from .models import *

admin.site.register(Movie)
admin.site.register(TopMovie)
admin.site.register(Genre)
admin.site.register(BookmarkMovie)