# Generated by Django 3.0.1 on 2019-12-27 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20191227_1733'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bookmarkmovie',
            table='bookmark_article',
        ),
    ]