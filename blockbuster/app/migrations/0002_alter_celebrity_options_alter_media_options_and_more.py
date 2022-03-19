# Generated by Django 4.0.3 on 2022-03-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='celebrity',
            options={'verbose_name': 'Знаменитость', 'verbose_name_plural': 'Знаменитости'},
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'Фото/Видео', 'verbose_name_plural': 'Фотки/Видео'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-created_at'], 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='filmography',
            field=models.ManyToManyField(blank=True, related_name='celebrities', to='app.movie', verbose_name='Фильмы с его участием'),
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='media',
            field=models.ManyToManyField(blank=True, related_name='celebrities', to='app.media'),
        ),
    ]