from dataclasses import fields
from rest_framework import serializers
from .models import PeriodDate

class PeriodDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodDate
        fields = '__all__'