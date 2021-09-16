from api.models import Gw2Key
from rest_framework import serializers

class Gw2KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gw2Key
        fields = ['key', 'name']
