# Generated by Django 3.0.1 on 2019-12-22 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20191222_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmarkmovie',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Movie', verbose_name='Фильм'),
        ),
    ]
