from rest_framework import serializers


class TelegramUserUnitListItemSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()


class TelegramUserUnitListOutputSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    units = serializers.ListField(child=TelegramUserUnitListItemSerializer())
