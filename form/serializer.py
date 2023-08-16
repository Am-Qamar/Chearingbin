from rest_framework import serializers
from .models import alist,blist,fields

class alistSerializer(serializers.ModelSerializer):
    class Meta:
        model = alist
        fields = '__all__'
class blistSerializer(serializers.ModelSerializer):
    class Meta:
        model = blist
        fields = '__all__'

class fieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = fields
        fields = ('id', 'name', 'new_name', 'hide')
class FieldUpdateSerializer(serializers.Serializer):
    fields = serializers.ListField(child=serializers.CharField())
class FieldUpdateSerializerV2(serializers.Serializer):
    fields = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )