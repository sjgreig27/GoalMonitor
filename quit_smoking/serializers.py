from rest_framework import serializers
from .models import *


class CigaretteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cigarette
        fields = ('cost_in_pounds', 'strength_in_mg', 'comment', 'timestamp', 'user')
        read_only_fields = ('timestamp',)


class CigarettePacketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CigarettePacket
        fields = ('cost_in_pounds', 'strength_in_mg', 'comment', 'timestamp', 'user')
        read_only_fields = ('timestamp',)


class VapourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vapour
        fields = ('cost_in_pounds', 'strength_in_mg', 'volume', 'comment', 'timestamp', 'user')
        read_only_fields = ('timestamp',)
