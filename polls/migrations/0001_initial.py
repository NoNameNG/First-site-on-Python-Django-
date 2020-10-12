# Generated by Django 3.0.1 on 2019-12-21 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameGenre', models.CharField(max_length=30, verbose_name='nameGenre')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('score', models.FloatField(verbose_name='score')),
                ('duration', models.IntegerField(verbose_name='duration')),
                ('year', models.IntegerField(verbose_name='year')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Genre', verbose_name='Genre')),
            ],
        ),
        migrations.CreateModel(
            name='TopMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Genre', verbose_name='Genre')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Movie', verbose_name='Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Recommended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Genre', verbose_name='Genre')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Movie', verbose_name='Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MyMovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Movie', verbose_name='add')),
            ],
        ),
    ]
