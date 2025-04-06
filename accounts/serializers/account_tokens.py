from rest_framework import serializers


class AccountTokenRetrieveOutputSerializer(serializers.Serializer):
    account_id = serializers.CharField()
    access_token = serializers.CharField()
