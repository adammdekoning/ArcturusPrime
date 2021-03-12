from django.shortcuts import render
from backEnd.serializers import ResultSerializer
from frontEnd.models import Result
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def testView(request):

    return render(request, 'backEnd/testPage.html')


@api_view(['GET'])
def ergResultList(request):

    results = Result.objects.filter(session__type='erg').order_by('-session__date')
    serializer = ResultSerializer(results, many=True)

    return Response(serializer.data)
