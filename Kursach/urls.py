from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.urls import  include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('accounts/', include('django.contrib.auth.urls') )
]
