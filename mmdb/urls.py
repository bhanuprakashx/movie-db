from django.urls import path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns 

from main.views import MovieDetailsView, MoviesListView, NewReviewView

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', MoviesListView.as_view(), name='movies-list'),
    path('movie/<int:pk>/', MovieDetailsView.as_view(), name='movie-details'),
    path('movie/<int:movie_pk>/review/', NewReviewView.as_view(), name='new-review'),
    
)