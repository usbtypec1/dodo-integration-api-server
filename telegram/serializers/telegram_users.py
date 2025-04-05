from rest_framework import serializers


class TelegramUserRoleUpdateInputSerializer(serializers.Serializer):
    access_code = serializers.CharField()


class TelegramUserUnitSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    legacy_id = serializers.IntegerField()


class TelegramUserReportTypeSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()


class TelegramUserRoleSerializer(serializers.Serializer):
    name = serializers.CharField()
    units = TelegramUserUnitSerializer(many=True)
    report_types = TelegramUserReportTypeSerializer(many=True)


class TelegramUserRetrieveOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    username = serializers.CharField(allow_null=True)
    role = TelegramUserRoleSerializer(allow_null=True)


class TelegramUserUpsertInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, allow_null=True)


class TelegramUserUpsertOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    username = serializers.CharField(allow_null=True)
