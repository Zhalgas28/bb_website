from django.contrib import auth
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q

from .forms import UserRegistrationForm, UserLoginForm, ReviewsForm
from .models import Movie, Celebrity, Genre, Reviews


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


class CelebrityList(ListView):
    ''' Список знаменитостей '''
    model = Celebrity
    template_name = 'app/celebritylist.html'
    context_object_name = 'celebrities'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directors'] = Celebrity.objects.filter(profession__name='Режиссер')[:4]
        return context


class CelebritySingle(DetailView):
    ''' Старница знаменитости '''
    model = Celebrity
    template_name = 'app/celebritysingle.html'
    context_object_name = 'celebrity'

class FilterMoviesView(ListView):
    ''' Фильтрация фильмов '''

    model = Movie
    template_name = 'app/movielist.html'
    context_object_name = 'movies'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all().distinct()
        context['years'] = Movie.objects.all().values('year')
        return context

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


def add_review(request, id):
    ''' Добавление отзывов '''
    form = ReviewsForm(request.POST)
    movie = get_object_or_404(Movie, id=id)

    if form.is_valid():
        comment = Reviews()
        comment.movie = movie
        comment.user = auth.get_user(request)
        comment.text = form.cleaned_data['text']
        comment.save()
        return redirect(movie.get_absolute_url())
    return render(request, 'app/moviesingle.html')
