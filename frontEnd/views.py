from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from frontEnd.decorators import unauthenticated_user, restricted
from frontEnd.models import *
from django.contrib.auth.models import Group
from django.db.models import Avg, Count, Min, Sum

current_season = 2019
season_start_date = Season_Period.objects.filter(season=current_season).filter(period='pre-season').values_list('start_date')[0][0]


# Create your views here.
@unauthenticated_user
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('frontEnd:dashboard')
        else:
            messages.info(request, 'Login failed- please try again')

    return render(request, 'frontEnd/login.html')


@login_required(login_url='frontEnd:login')
def dashboard(request):


    group = request.user.groups.all()[0]

    context = {
    'group':str(group),
    }

    return render(request, 'frontEnd/dashboard.html', context)


@login_required(login_url='frontEnd:login')
def currentResults(request):

    group = request.user.groups.all()[0]

    context = {
    'group':str(group),
    }

    return render(request, 'frontEnd/current.html', context)


@login_required(login_url='frontEnd:login')
def historicResults(request):


    group = request.user.groups.all()[0]

    context = {
    'group':str(group),
    }


    return render(request, 'frontEnd/historic.html', context)

def logoutUser(request):

    logout(request)

    return redirect('frontEnd:login')


@login_required(login_url='frontEnd:login')
@restricted(allowed_roles=['Athlete'])
def profilePage(request):

    group = request.user.groups.all()[0]

    personal_bests = {}
    for distance in Result.objects.filter(crew__id=request.user.athlete.id).values_list('distance').order_by('distance').distinct():
        personal_best = Result.objects.filter(crew__id=request.user.athlete.id).filter(distance=distance[0]).order_by('time')[0]
        personal_bests[distance[0]]=personal_best

    recent_ergs = Result.objects.filter(crew__id=request.user.athlete.id).order_by('-session__date')[:5]

    distances = {}
    periods = [('This Season', season_start_date), ('Lifetime', '2000-01-01')]

    for period in periods:
        period_dict = {}
        query_set = Distance_Data.objects.filter(athlete__id=request.user.athlete.id).filter(date__gte=period[1])
        for type in query_set.values_list('type').distinct():
            period_dict[type[0]] = query_set.filter(type=type[0]).aggregate(Sum('distance'))['distance__sum']
        distances[period[0]] = period_dict

    context = {
    'group':str(group),
    'personal_bests':personal_bests,
    'recent_ergs':recent_ergs,
    'distances':distances,
    }

    return render(request, 'frontEnd/profile.html', context)

@login_required(login_url='frontEnd:login')
@restricted(allowed_roles=['Coach', 'Coordinator'])
def analysis(request):

    context = {}

    return render(request, 'frontEnd/analysis.html', context)
