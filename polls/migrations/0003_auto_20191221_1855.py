# Generated by Django 3.0.1 on 2019-12-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_topmovie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topmovie',
            name='image',
            field=models.ImageField(upload_to='polls/static/images/', verbose_name='Image'),
        ),
    ]