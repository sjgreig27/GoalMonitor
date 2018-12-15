from rest_framework import serializers
from .models import *


class MeasurementTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MeasurementType
        fields = ('name', 'unit')


class MeasurementSerializer(serializers.HyperlinkedModelSerializer):

    measurement = serializers.PrimaryKeyRelatedField(write_only=True, queryset=MeasurementType.objects.all())
    measurement_type = MeasurementTypeSerializer(many=False, read_only=True, source='measurement')

    class Meta:
        model = Measurement
        fields = ('measurement', 'measurement_type', 'quantity', 'timestamp')
