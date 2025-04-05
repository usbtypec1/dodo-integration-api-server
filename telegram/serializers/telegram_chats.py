from rest_framework import serializers


class TelegramChatUpsertInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255, allow_null=True)
    username = serializers.CharField(max_length=255, allow_null=True)


class TelegramChatUpsertOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(allow_null=True)
    username = serializers.CharField(allow_null=True)
