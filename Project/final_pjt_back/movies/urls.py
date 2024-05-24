from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies),
    path('actors/', views.all_actors),
    path('genres/', views.all_genres),
    path('recommended/', views.recommended_movies),
    path('hashtag/', views.get_hashtag),
    path('hashtag_to_movie/', views.hashtag_to_movie),
    path('<int:movie_pk>/review/', views.create_review),
    path('<int:movie_pk>/get_review/', views.movie_reviews),
    path('reviews/', views.personal_reviews),
    path('<int:movie_pk>/review/<int:review_pk>/', views.review),
    path('<int:movie_pk>/like/', views.like_movie),
]
