from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.user_detail),
    path('nickname/', views.edit_nickname),
    path('prefer/', views.edit_preference),
    path('password_check/', views.password_check),
    path('signout/', views.sign_out),
]
