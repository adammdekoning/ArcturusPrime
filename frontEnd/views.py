from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from frontEnd.decorators import unauthenticated_user, coach_restricted
from frontEnd.models import *
from django.contrib.auth.models import Group


# Create your views here.

@login_required(login_url='frontEnd:login')
def dashboard(request):


    group = request.user.groups.all()[0]
    print(str(group) == 'Coordinator')

    context = {
    'group':str(group),
    }

    return render(request, 'frontEnd/dashboard.html', context)


@login_required(login_url='frontEnd:login')
def currentResults(request):

    return render(request, 'frontEnd/current.html')


@login_required(login_url='frontEnd:login')
@coach_restricted(allowed_roles=['Coach', 'Coordinator'])
def historicResults(request):

    return render(request, 'frontEnd/historic.html')

def logoutUser(request):

    logout(request)

    return redirect('frontEnd:login')


@unauthenticated_user
def loginPage(request):

    context = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('frontEnd:dashboard')
        else:
            messages.info(request, 'Login failed- please try again')

    return render(request, 'frontEnd/login.html', context)
