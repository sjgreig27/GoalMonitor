from django.conf.urls import url, include
from rest_framework import routers
from .views import MeasurementTypeViewSet, MeasurementViewSet

router = routers.DefaultRouter()
router.register(r'measurement', MeasurementViewSet)
router.register(r'measurement_type', MeasurementTypeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]