from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.name


class Squad(models.Model):
    name = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.name


class Athlete(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=256, null=False)
    email = models.CharField(max_length=256, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    year_seven_year = models.PositiveIntegerField(null=True) # first year rowing, used to calculate current year group
    club = models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)
    squad = models.ForeignKey(Squad, null=True, blank=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=False)

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


class Session_Data(models.Model):
    TYPE = {
        ('rowing','rowing'),
        ('erg','erg'),
        ('running','running'),
        ('swimming','swimming'),
        ('strength','strength'),
        ('active recovery','active recovery'),
        ('bike','bike'),
        ('cross training','cross training'),
    }

    date = models.DateField()
    type = models.CharField(max_length=256, null=True, choices=TYPE, blank=True)
    notes = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(str(self.date) + ' ' + str(self.type))


class Result(models.Model):
     BOAT_CLASS = {
        ('1x','1x'),
        ('2x','2x'),
        ('2-','2-'),
        ('4x', '4x'),
        ('4x+','4x+'),
        ('4-','4-'),
        ('4+','4+'),
        ('8+','8+'),
     }
     session = models.ForeignKey(Session_Data, on_delete=models.CASCADE)
     distance = models.PositiveIntegerField()
     time = models.TimeField()
     crew = models.ManyToManyField(Athlete)
     rate = models.CharField(max_length=20, null=True, blank=True)
     notes = models.CharField(max_length=256, null=True, blank=True)
     boat_class = models.CharField(max_length=10, null=True, choices=BOAT_CLASS, blank=True)


class Distance_Data(models.Model):
    BOAT_CLASS = {
        ('1x','1x'),
        ('2x','2x'),
        ('2-','2-'),
        ('4x', '4x'),
        ('4x+','4x+'),
        ('4-','4-'),
        ('4+','4+'),
        ('8+','8+'),
    }
    TYPE = {
        ('rowing','rowing'),
        ('erg','erg'),
        ('running','running'),
        ('swimming','swimming'),
        ('strength','strength'),
        ('active recovery','active recovery'),
        ('bike','bike'),
        ('cross training','cross training'),
    }
    athlete = models.ForeignKey(Athlete, blank=False, null=False, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    boat_class = models.CharField(max_length=10, null=True,blank=True, choices=BOAT_CLASS)
    distance = models.PositiveIntegerField()
    time = models.TimeField(blank=True, null=True)
    rate = models.CharField(max_length=20, null=True, blank=True)
    notes = models.CharField(max_length=256, null=True, blank=True)
    type = models.CharField(max_length=256, null=True, blank=True, choices=TYPE)

    def __str__(self):
        return str(str(self.athlete) + ' ' + str(self.type) + ' ' + str(self.date))


class Season_Period(models.Model):
    period = models.CharField(null=False, blank=False, max_length=256)
    season = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return str(str(self.season) + ' ' + self.period)
