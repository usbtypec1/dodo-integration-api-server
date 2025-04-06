from rest_framework import serializers


class ReportRouteListInputSerializer(serializers.Serializer):
    unit_id = serializers.UUIDField(default=None)
    report_type_id = serializers.CharField(default=None)
    chat_id = serializers.IntegerField(default=None)
    take = serializers.IntegerField(default=100, min_value=1, max_value=1000)
    skip = serializers.IntegerField(default=0, min_value=0)


class ReportRouteListItemSerializer(serializers.Serializer):
    unit_id = serializers.UUIDField()
    report_type_id = serializers.CharField()
    report_type_name = serializers.CharField()
    chat_id = serializers.IntegerField()


class ReportRouteListOutputSerializer(serializers.Serializer):
    routes = ReportRouteListItemSerializer(many=True)
    is_end_of_list_reached = serializers.BooleanField()


class ReportRouteCreateInputSerializer(serializers.Serializer):
    unit_legacy_id = serializers.IntegerField()
    report_type_id = serializers.CharField()
    chat_id = serializers.IntegerField()


class ReportRouteDeleteInputSerializer(serializers.Serializer):
    unit_legacy_id = serializers.IntegerField()
    report_type_id = serializers.CharField()
    chat_id = serializers.IntegerField()
