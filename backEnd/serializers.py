from rest_framework import serializers
from frontEnd.models import Session_Data, Result, Athlete


class ResultSerializer(serializers.ModelSerializer):
    date = serializers.DateField(source="session.date", read_only=True)
    crew = serializers.StringRelatedField(many=True)
    # crew_names = serializers.CharField(read_only=True, source="Athlete.name")
    class Meta:
        model = Result
        fields = ['date',
        'crew',
        'distance',
        'time',
        'rate',
        'notes']
