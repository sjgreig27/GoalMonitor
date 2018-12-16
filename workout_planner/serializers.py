from rest_framework import serializers
from .models import *


class LiftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lift
        fields = ('id', 'name')


class WorkoutPlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = ('id', 'name')


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):

    plan_def = WorkoutPlanSerializer(many=False, read_only=True, source='plan')
    plan = serializers.PrimaryKeyRelatedField(write_only=True, queryset=WorkoutPlan.objects.all())

    class Meta:
        model = Workout
        fields = ('id', 'day', 'plan', 'plan_def')


class PlannedLiftSerializer(serializers.HyperlinkedModelSerializer):

    lift_type = LiftSerializer(many=False, read_only=True, source='lift')
    lift = serializers.PrimaryKeyRelatedField(many=False, queryset=Lift.objects.all(), write_only=True)
    workout_def = WorkoutSerializer(many=False, read_only=True, source='workout')
    workout = serializers.PrimaryKeyRelatedField(many=False, queryset=Workout.objects.all(), write_only=True)

    class Meta:
        model = PlannedLift
        fields = ('id', 'lift', 'lift_type', 'workout', 'workout_def')


class LiftRecordSerializer(serializers.HyperlinkedModelSerializer):

    planned_lift_def = PlannedLiftSerializer(many=False, read_only=True, source='planned_lift')
    planned_lift = serializers.PrimaryKeyRelatedField(many=False, queryset=PlannedLift.objects.all(), write_only=True)

    class Meta:
        model = LiftRecord
        fields = ('id', 'planned_lift', 'planned_lift_def', 'timestamp', 'user')


class SetSerializer(serializers.HyperlinkedModelSerializer):

    lift_def = LiftRecordSerializer(many=False, read_only=True, source='lift')
    lift = serializers.PrimaryKeyRelatedField(many=False, queryset=LiftRecord.objects.all(), write_only=True)

    class Meta:
        model = Set
        fields = ('id', 'lift', 'lift_def', 'number_of_reps', 'weight_in_kg')

