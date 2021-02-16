from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from frontEnd.models import Athlete, Coach, Club, Coordinator

apps = [Athlete, Coach, Club, Coordinator]

# Register your models here.

for app in apps:
    admin.site.register(app)
