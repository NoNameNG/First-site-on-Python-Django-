from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    nameGenre = models.CharField(max_length=30, verbose_name="nameGenre")

class Movie(models.Model):
    name = models.CharField(max_length=30, verbose_name="name")
    score = models.FloatField(verbose_name="score")
    duration = models.IntegerField(verbose_name="duration")
    year = models.IntegerField(verbose_name="year")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Genre")


class TopMovie(models.Model):
    image = models.ImageField(upload_to = "polls/static/images/", verbose_name= "Image")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Genre")


class BookmarkBase(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return self.user.username


class BookmarkMovie(BookmarkBase):
    class Meta:
        db_table = "bookmark_article"

    obj = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")


