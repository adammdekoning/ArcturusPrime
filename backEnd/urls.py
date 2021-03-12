from django.urls import include, path
from rest_framework import routers
from backEnd import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'backEnd'

urlpatterns = [
    path('testPage/', views.testView, name='tester'),
    path('ergResultsList/', views.ergResultList, name='ergResultList'),
]
