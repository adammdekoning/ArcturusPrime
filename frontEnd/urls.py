from django.urls import path, include
from frontEnd import views

app_name = 'frontEnd'

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('current-results/', views.currentResults, name='currentResults'),
    path('historic-erg-results/', views.historicErgResults, name='historicErgResults'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/<int:pk>', views.profilePage, name='profile'),
    path('analysis/', views.analysis, name='analysis'),
    path('athlete-list/', views.athleteList, name='athleteList'),
    path('session/<int:pk>', views.sessionResults, name='sessionResults'),
]
