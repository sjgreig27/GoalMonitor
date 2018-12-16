from django.conf.urls import url, include
from rest_framework import routers
from .views import CigaretteViewSet, CigarettePacketViewSet, VapourViewSet

router = routers.DefaultRouter()
router.register(r'cigarette', CigaretteViewSet)
router.register(r'cigarette-packet', CigarettePacketViewSet)
router.register(r'vapour', VapourViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]