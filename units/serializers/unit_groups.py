from rest_framework import serializers


class UnitGroupListOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
