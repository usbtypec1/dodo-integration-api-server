from rest_framework import serializers


class UnitListInputSerializer(serializers.Serializer):
    group_id = serializers.IntegerField(default=None)


class UnitListOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    legacy_id = serializers.IntegerField()
    group_id = serializers.IntegerField()
    group_name = serializers.CharField()
    office_manager_account_id = serializers.CharField()
    shift_manager_account_id = serializers.CharField()
    dodo_is_api_account_id = serializers.CharField()
