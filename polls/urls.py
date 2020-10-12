from django.conf.urls import url
from . import views
from django.urls import include
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = 'ajax'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'movie', views.getinfoMovie),
    url(r'genre', views.getinfoGenre),
    url(r'top', views.getinfoTopMovie),
    url(r'login', views.LoginFormView.as_view()),
    url(r'logout',views.LogoutView.as_view()),
    url(r'^registration/$', views.RegisterFormView.as_view()),
    url(r'favorite',  login_required(views.BookmarkView.as_view()), name='mymovies'),
]