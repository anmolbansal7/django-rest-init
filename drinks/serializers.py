from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:  # metadata descr model
        model = Drink
        fields = ['id', 'name', 'description']
