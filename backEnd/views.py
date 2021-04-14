from django.shortcuts import render
from backEnd.serializers import ResultSerializer
from frontEnd.models import Result, Session_Data, Athlete
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg, Count, Min, Sum
from frontEnd.func import avgTime, avgSplit
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def testView(request):

    return render(request, 'backEnd/testPage.html')


@api_view(['GET'])
def ergResultList(request):

    results = Result.objects.filter(session__type='erg').order_by('-session__date')
    serializer = ResultSerializer(results, many=True)

    return Response(serializer.data)


@login_required
def session_results_json(request,pk):
    session_results = []

    session = Result.objects.filter(session__id=pk)


    for distance in session.values_list('distance').order_by('distance').distinct():
        for crew in session.filter(distance=distance[0]).values_list('crew').distinct():
            crew_results_dict = {}
            crew_times = []

            for time in session.filter(distance=distance[0]).filter(crew=crew[0]).order_by('piece_number').values_list('time'):
                crew_times.append(time[0])

            crew_average = avgTime(crew_times)
            crew_average_split = avgSplit(crew_average, distance[0])

            crew_results_dict['crew'] = Athlete.objects.get(id=crew[0]).name
            crew_results_dict["distance"]=distance[0]
            crew_results_dict['pieces']=len(crew_times)
            crew_results_dict['average_time']=crew_average
            crew_results_dict['average_split']=crew_average_split
            for i in range(len(crew_times)):
                crew_results_dict['piece_{}'.format(i+1)]=crew_times[i]

            session_results.append(crew_results_dict)






    return JsonResponse(session_results, safe=False)#, cls=DjangoJSONEncoder)
