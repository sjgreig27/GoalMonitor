from django.conf.urls import url, include
from rest_framework import routers
from .views import LiftSerializerViewSet, WorkoutPlanSerializerViewSet, WorkoutSerializerViewSet, \
    PlannedLiftSerializerViewSet, LiftRecordSerializerViewSet, SetSerializerViewSet

router = routers.DefaultRouter()
router.register(r'lift', LiftSerializerViewSet)
router.register(r'workout-plan', WorkoutPlanSerializerViewSet)
router.register(r'workout', WorkoutSerializerViewSet)
router.register(r'planned-lift', PlannedLiftSerializerViewSet)
router.register(r'lift-record', LiftRecordSerializerViewSet)
router.register(r'set', SetSerializerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]