from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from frontEnd.models import (Athlete, Coach, Club, Coordinator, Squad,
Session_Data, Result, Distance_Data, Season_Period)

apps = [Athlete, Coach, Club, Coordinator, Squad, Session_Data,
 Result, Distance_Data, Season_Period]

# Register your models here.

for app in apps:
    admin.site.register(app)
