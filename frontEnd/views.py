from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from frontEnd.decorators import unauthenticated_user, restricted
from frontEnd.models import *
from django.contrib.auth.models import Group
from django.db.models import Avg, Count, Min, Sum
from frontEnd.func import avgTime, avgSplit
import json
from django.core.serializers.json import DjangoJSONEncoder

current_season = 2019
season_start_date = Season_Period.objects.filter(season=current_season).filter(period='pre-season').values_list('start_date')[0][0]
season_end_date = Season_Period.objects.filter(season=current_season).filter(period='term one').values_list('end_date')[0][0]

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

    sessions = Session_Data.objects.filter(date__gte=season_start_date, date__lte=season_end_date).order_by('-date')

    context = {
    'group':str(group),
    'sessions':sessions,
    'current_season':current_season,
    }

    return render(request, 'frontEnd/current.html', context)


@login_required
def sessionResults(request, pk):


    session_results = {}

    group = request.user.groups.all()[0]

    session_info = Session_Data.objects.get(id=pk)

    session = Result.objects.filter(session__id=pk)

    for distance in session.values_list('distance').order_by('distance').distinct():
        cols = []
        distance_results = {}
        for crew in session.filter(distance=distance[0]).values_list('crew'):
            crew_results_dict = {}
            crew_times = []
            for time in session.filter(distance=distance[0]).filter(crew=crew[0]).order_by('piece_number').values_list('time'):
                crew_times.append(time[0])

            for piece_number in session.filter(distance=distance[0]).filter(crew=crew[0]).values_list('piece_number'):
                if piece_number[0] not in cols:
                    cols.append(piece_number[0])

            crew_average = avgTime(crew_times)
            crew_average_split = avgSplit(crew_average, distance[0])

            crew_results_dict['average']=[crew_average]
            crew_results_dict['average_split']=[crew_average_split]
            crew_results_dict['results']=crew_times

            distance_results[Athlete.objects.get(id=crew[0]).name] = crew_results_dict

        for crew, crew_results in distance_results.items():
            if len(crew_results['results']) < len(cols):
                for i in range(len(cols) - len(crew_results['results'])):
                    crew_results['results'].append('-')

        session_results[distance[0]] = distance_results
    #
    # jsi = json.dumps(session_results, cls=DjangoJSONEncoder)
    #
    # print(jsi)

    context = {
    'group':str(group),
    'session_results':session_results,
    'session':session,
    'cols':cols,
    'session_info':session_info,
    }

    return render(request, 'frontEnd/session.html', context)


@login_required(login_url='frontEnd:login')
def historicErgResults(request):


    group = request.user.groups.all()[0]

    context = {
    'group':str(group),
    }

    return render(request, 'frontEnd/historicErg.html', context)


def logoutUser(request):

    logout(request)

    return redirect('frontEnd:login')


@login_required(login_url='frontEnd:login')
def profilePage(request, pk):

    group = str(request.user.groups.all()[0])

    if group == 'Coordinator' or group == 'Coach':
        id_filter = pk

    elif group == 'Athlete':
        id_filter = request.user.athlete.id

    athlete = Athlete.objects.get(id=id_filter)

    personal_bests = {}
    for distance in Result.objects.filter(crew__id=id_filter).filter(session__type='erg').values_list('distance').order_by('distance').distinct():
        personal_best = Result.objects.filter(crew__id=id_filter).filter(distance=distance[0]).order_by('time')[0]
        personal_bests[distance[0]]=personal_best

    recent_ergs = Result.objects.filter(crew__id=id_filter).order_by('-session__date')[:5]

    distances = {}
    periods = [('{} Season'.format(current_season), season_start_date), ('Lifetime', '2000-01-01')]

    for period in periods:
        period_dict = {}
        query_set = Distance_Data.objects.filter(athlete__id=id_filter).filter(date__gte=period[1])
        for type in query_set.values_list('type').distinct():
            period_dict[type[0]] = query_set.filter(type=type[0]).aggregate(Sum('distance'))['distance__sum']
        distances[period[0]] = period_dict

    session_log = Distance_Data.objects.filter(athlete__id=id_filter).order_by('-date')[:5]

    context = {
    'athlete':athlete,
    'group':group,
    'personal_bests':personal_bests,
    'recent_ergs':recent_ergs,
    'distances':distances,
    'session_log': session_log,
    }

    return render(request, 'frontEnd/profile.html', context)


@login_required(login_url='frontEnd:login')
@restricted(allowed_roles=['Coach', 'Coordinator'])
def analysis(request):

    context = {}

    return render(request, 'frontEnd/analysis.html', context)


@login_required(login_url='frontEnd:login')
@restricted(allowed_roles=['Coach', 'Coordinator'])
def athleteList(request):

    group = request.user.groups.all()[0]
    # The request.user.club.id is being used to stop a users from being able to see results from different school/clubs
    try:
        full_squad = Athlete.objects.filter(active=True).filter(club__id=request.user.coach.club.id).order_by('name')
    except:
        full_squad = Athlete.objects.filter(active=True).filter(club__id=request.user.coordinator.club.id).order_by('name')

    senior_squad = full_squad.filter(year_seven_year__lte=(current_season-3)).order_by('name')
    inter_squad = full_squad.filter(year_seven_year = (current_season-2)).order_by('name')
    junior_squad = full_squad.filter(year_seven_year__gte = (current_season - 1)).order_by('name')

    context = {
    'group':str(group),
    'current_season':current_season,
    'full_squad':full_squad,
    'senior_squad':senior_squad,
    'inter_squad':inter_squad,
    'junior_squad':junior_squad,
    }

    return render(request, 'frontEnd/athleteList.html', context)
