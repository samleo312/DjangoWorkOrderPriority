from rest_framework import serializers
from .models import Resource, UnaddedWorkOrder, AddedWorkOrder

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class UnaddedWorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnaddedWorkOrder
        fields = '__all__'

class AddedWorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddedWorkOrder
        fields = '__all__'