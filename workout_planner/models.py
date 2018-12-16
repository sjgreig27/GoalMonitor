from django.db import models
from django.contrib.auth.models import User

# Create your models here.

WEEKDAYS = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday')
)


class Lift(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):

    name = models.CharField(max_length=280)

    def __str__(self):
        return self.name


class Workout(models.Model):

    day = models.CharField(max_length=10, choices=WEEKDAYS)
    plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('day', 'plan')

    def __str__(self):
        return self.plan.name + ' (' + self.day + ')'


class PlannedLift(models.Model):

    lift = models.ForeignKey(Lift, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return self.lift.name + ' (' + self.workout.plan.name + ': ' + self.workout.day + ')'


class LiftRecord(models.Model):

    planned_lift = models.ForeignKey(PlannedLift, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.planned_lift.lift.name + ' (' + self.planned_lift.workout.day + ')'


class Set(models.Model):

    lift = models.ForeignKey(LiftRecord, on_delete=models.CASCADE)
    number_of_reps = models.IntegerField()
    weight_in_kg = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.lift.__str__() + ' [' + str(self.number_of_reps) + ' x ' + str(self.weight_in_kg) + ']'


