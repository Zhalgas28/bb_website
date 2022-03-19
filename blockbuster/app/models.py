from django.db import models
from django.urls import reverse_lazy

class Genre(models.Model):
    ''' Жанры '''
    name = models.CharField('Имя', max_length=155)
    slug = models.CharField('url', unique=True, max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Profession(models.Model):
    ''' Профессии '''
    name = models.CharField('Имя', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профессию'
        verbose_name_plural = 'Профессии'


class Media(models.Model):
    ''' Фотки и видео '''
    name = models.CharField('Имя', max_length=155)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото/Видео'
        verbose_name_plural = 'Фотки/Видео'


class Celebrity(models.Model):
    ''' Знаменитости '''
    name = models.CharField('Имя', max_length=155)
    slug = models.CharField('url', unique=True, max_length=155)
    profession = models.ForeignKey(Profession, on_delete=models.PROTECT, related_name='celebrities',
                                   verbose_name='Профессия')
    description = models.TextField('Описание')
    media = models.ManyToManyField(Media, related_name='celebrities', blank=True)
    filmography = models.ManyToManyField('Movie', verbose_name='Фильмы с его участием', related_name='celebrities', blank=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m/%d')
    biography = models.TextField(verbose_name='Биография')
    date_of_birth = models.CharField('Дата рождения', max_length=155, help_text='Пример: "22 Июня, 2022 года')
    country = models.CharField(verbose_name='Страна', max_length=155, default='USA')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Знаменитость'
        verbose_name_plural = 'Знаменитости'

    def get_absolute_url(self):
        return reverse_lazy('celebritysingle', kwargs={'slug': self.slug})


class Movie(models.Model):
    ''' Фильмы '''
    name = models.CharField('Имя', max_length=155)
    slug = models.CharField('url', unique=True, max_length=155)
    genre = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='movies')
    year = models.PositiveSmallIntegerField('Год выхода', default=2022)
    release_date = models.DateField('Дата выхода')
    run_time = models.CharField('Длительность', max_length=155, help_text='Пример: 2 часа 15 минут')
    director = models.ForeignKey(Celebrity, on_delete=models.SET_NULL, null=True, verbose_name='режиссер')
    actors = models.ManyToManyField(Celebrity, verbose_name='Актеры', related_name='movies')
    media = models.ManyToManyField(Media, related_name='movies')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    trailer = models.URLField(verbose_name='Трейлер', help_text='Введите ссылку трейлера', default='https://youtube.com')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse_lazy('moviesingle', kwargs={'slug': self.slug})


class RatingStar(models.Model):
    ''' Звезды рейтинга '''
    star = models.PositiveSmallIntegerField(default=0, verbose_name='звезда')

    class Meta:
        verbose_name = 'Звезда(у)'
        verbose_name_plural = 'Звезды'


class Rating(models.Model):
    ''' Рейтинг '''
    ip = models.CharField('IP адрес', max_length=155)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        return f"{self.movie} - {self.star}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    name = models.CharField('Имя', max_length=155)
    email = models.EmailField()
    text = models.TextField('Текст', max_length=10000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено в')


    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'