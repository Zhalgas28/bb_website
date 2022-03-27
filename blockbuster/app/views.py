from statistics import mean

from django.contrib import auth
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q, Count, Avg

from .forms import UserRegistrationForm, UserLoginForm, ReviewsForm, RatingForm
from .models import Movie, Celebrity, Genre, Reviews, Profession, Rating
from .service import calc_avg_rating


class Index(ListView):
    ''' Главная страница '''

    model = Movie
    template_name = 'app/index.html'
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['celebrities'] = Celebrity.objects.order_by('-name')[:4]
        return context

    def get_queryset(self):
        return Movie.objects.order_by('created_at')[:8]


class MovieList(ListView):
    ''' Список фильмов '''

    model = Movie
    template_name = 'app/movielist.html'
    context_object_name = 'movies'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all().distinct()
        context['years'] = Movie.objects.all().values('year')
        return context


class AllMovie(ListView):
    ''' Все фильмы '''

    model = Movie
    template_name = 'app/allmovie.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AllMovie, self).get_context_data(**kwargs)
        context['count'] = Movie.objects.all().count()
        return context


class MovieSingle(DetailView):
    ''' Страница фильма '''
    model = Movie
    template_name = 'app/moviesingle.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        context['avg'] = calc_avg_rating(self.object.id)

        # Получение похожих фильмов
        movie_tags_ids = self.object.genre.values_list('id', flat=True)
        similar_movies = Movie.objects.filter(genre__in=movie_tags_ids).exclude(id=self.object.id)
        context['similar_movies'] = similar_movies.annotate(same_genres=Count('genre')).order_by('-same_genres', '-created_at')[:4]

        return context


class CelebrityList(ListView):
    ''' Список знаменитостей '''
    model = Celebrity
    template_name = 'app/celebritylist.html'
    context_object_name = 'celebrities'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directors'] = Celebrity.objects.filter(profession__name='Режиссер')[:4]
        context['professions'] = Profession.objects.all()
        return context


class CelebritySingle(DetailView):
    ''' Старница знаменитости '''
    model = Celebrity
    template_name = 'app/celebritysingle.html'
    context_object_name = 'celebrity'


class FilterMoviesView(MovieList, ListView):
    ''' Фильтрация фильмов '''

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(name__icontains=self.request.GET.get("Имя")) |
            Q(genre__in=self.request.GET.getlist('genre')) |
            Q(year__range=(int(self.request.GET.get('year1')), int(self.request.GET.get('year2'))))
        )
        return queryset


def user_register(request):
    ''' Регистрация пользователей '''
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'app/register.html', {'form': form, 'res': 'Ошибка регистрации'})


def user_login(request):
    ''' Аутентификация '''
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
        return render(request, 'app/login.html', {'form': form})


def user_logout(request):
    ''' Выход с учетной записи '''
    logout(request)
    return redirect('login')


def add_review(request, slug):
    ''' Добавление отзывов '''
    form = ReviewsForm(request.POST)
    movie = get_object_or_404(Movie, slug=slug)

    if form.is_valid():
        comment = Reviews()
        comment.movie = movie
        comment.user = auth.get_user(request)
        comment.text = form.cleaned_data['text']
        comment.save()
        return redirect(movie.get_absolute_url())
    return redirect(movie.get_absolute_url())


class FilterCelebritiesList(CelebrityList, ListView):
    ''' Фильтр знаменитостей '''

    def get_queryset(self):
        queryset = Celebrity.objects.filter(
            Q(name__icontains=self.request.GET.get('name')) |
            Q(profession__in=self.request.GET.getlist('professions'))
        )
        return queryset


class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
