from rest_framework import viewsets
from .serializers import MeasurementTypeSerializer, MeasurementSerializer
from .models import MeasurementType, Measurement

# Create your views here.


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementTypeViewSet(viewsets.ModelViewSet):
    queryset = MeasurementType.objects.all()
    serializer_class = MeasurementTypeSerializer
