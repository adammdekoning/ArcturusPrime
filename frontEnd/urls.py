from django.urls import path, include
from frontEnd import views

app_name = 'frontEnd'

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('current-results/', views.currentResults, name='currentResults'),
    path('historic-results/', views.historicResults, name='historicResults'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profilePage, name='profile'),
    path('analysis/', views.analysis, name='analysis'),
]
