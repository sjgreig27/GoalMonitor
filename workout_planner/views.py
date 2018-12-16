from rest_framework import viewsets
from .serializers import LiftSerializer, WorkoutPlanSerializer, WorkoutSerializer, PlannedLiftSerializer, \
    LiftRecordSerializer, SetSerializer
from .models import Lift, Set, Workout, WorkoutPlan, PlannedLift, LiftRecord

# Create your views here.


class LiftSerializerViewSet(viewsets.ModelViewSet):
    queryset = Lift.objects.all()
    serializer_class = LiftSerializer


class WorkoutPlanSerializerViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer


class WorkoutSerializerViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class PlannedLiftSerializerViewSet(viewsets.ModelViewSet):
    queryset = PlannedLift.objects.all()
    serializer_class = PlannedLiftSerializer


class LiftRecordSerializerViewSet(viewsets.ModelViewSet):
    queryset = LiftRecord.objects.all()
    serializer_class = LiftRecordSerializer


class SetSerializerViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer

