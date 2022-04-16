from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('filter_movies/', FilterMoviesView.as_view(), name='filter_movies'),
    path('filter_celebrities', FilterCelebritiesList.as_view(), name='filter_celebrities'),
    path('movies/', MovieList.as_view(), name='movies'),
    path('allmovies/', AllMovie.as_view(), name='allmovies'),
    path('movies/<str:slug>/', MovieSingle.as_view(), name='moviesingle'),
    path('celebrities/', CelebrityList.as_view(), name='celebritylist'),
    path('celebrity/<str:slug>/', CelebritySingle.as_view(), name='celebritysingle'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('addreview/<str:slug>/', add_review, name='addreview'),
    path('addrating/', AddStarRating.as_view(), name='addrating'),
    path('delete_review/<int:pk>/', delete_review, name='delete_review')
]
