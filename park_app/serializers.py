from rest_framework import serializers

from .models import Ivent, Creater


class IventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ivent
        fields = '__all__'


class CreaterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Creater
        fields = '__all__'