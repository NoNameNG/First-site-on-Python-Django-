from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib import auth
#from pip._vendor.requests import auth
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
import json



def index(request):
    return render(request, "index.html")


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)



class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")


def getinfoGenre(request):
    genre = Genre.objects.all()
    print(genre)
    return render(request, "index.html", {'genre': genre})


def getinfoTopMovie(request):
    top = TopMovie.objects.all()
    print(top)
    return render(request, "topmovie.html", {'top': top})


def getinfoMovie(request):
    movie = Movie.objects.all()
    print(movie)
    return render(request, "movie.html", {'movie': movie})


def postinfoMovie(request):
    if request.method == "POST":
        movie = Movie()
        movie.name = request.POST.get("movie_name")
        movie.genre = request.POST.get("movie_genre")
        movie.score = request.POST.get("movie_score")
        movie.duration = request.POST.get("movie_duration")
        movie.year = request.POST.get("movie_duration")
        movie.save()
    return HttpResponseRedirect("/movie")


def postinfoTopMovie(request):
    if request.method == "POST":
        top = TopMovie()
        top.movie = request.POST.get("topmovie_movie")
        top.genre = request.POST.get("topmovie_genre")
        top.image = request.POST.get("topmovie_image")
        top.save()
    return HttpResponseRedirect("/topmovie")


class BookmarkView(View):

    def post(self, request):
        fav = BookmarkMovie()

        id = request.GET.get("id")
        fav.obj = Movie.objects.get(pk = id)


        user = request.user
        fav.user = user
        fav.save()

        return HttpResponseRedirect("/favorite")

    def get(self, request):
        favorite = BookmarkMovie.objects.all()
        print(favorite)
        return render(request, "mymovies.html", {'favorite': favorite})
