from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.name


class Athlete(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=256, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    year_seven_year = models.PositiveIntegerField(null=True) # first year rowing, used to calculate current year group
    club = models.OneToOneField(Club, null=True, on_delete=models.SET_NULL)
    squad = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name


class Coach(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=256, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    club = models.OneToOneField(Club, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Coordinator(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=256, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    club = models.OneToOneField(Club, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
