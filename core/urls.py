from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('about-us/', views.about_us, name='about_us'),
    path('player/<str:video_id>/', views.open_player, name='open_player'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('search/<str:query>', views.search, name='search'),
]