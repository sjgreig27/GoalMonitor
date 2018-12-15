from rest_framework import viewsets
from .serializers import CigaretteSerializer, CigarettePacketSerializer, VapourSerializer
from .models import Cigarette, CigarettePacket, Vapour

# Create your views here.


class CigaretteViewSet(viewsets.ModelViewSet):
    queryset = Cigarette.objects.all()
    serializer_class = CigaretteSerializer


class CigarettePacketViewSet(viewsets.ModelViewSet):
    queryset = CigarettePacket.objects.all()
    serializer_class = CigarettePacketSerializer


class VapourViewSet(viewsets.ModelViewSet):
    queryset = Vapour.objects.all()
    serializer_class = VapourSerializer

