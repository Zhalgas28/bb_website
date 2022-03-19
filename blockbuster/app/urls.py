from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('filter/', FilterMoviesView.as_view(), name='filter'),
    path('movies/', MovieList.as_view(), name='movies'),
    path('allmovies/', AllMovie.as_view(), name='allmovies'),
    path('movies/<str:slug>/', MovieSingle.as_view(), name='moviesingle'),
    path('celebrities/', CelebrityList.as_view(), name='celebritylist'),
    path('celebrity/<str:slug>/', CelebritySingle.as_view(), name='celebritysingle'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('addreview/<int:id>/', add_review, name='addreview')
]
