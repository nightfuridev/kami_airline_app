from rest_framework import serializers
from .models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):
   class Meta:
       model = Airplane
       fields = ['id', 'passengers', 'fuel_tank_capacity', 'fuel_consumption_per_minute', 'max_minutes_to_fly']