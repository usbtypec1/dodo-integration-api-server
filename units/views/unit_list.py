from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from units.serializers import (
    UnitListInputSerializer,
    UnitListOutputSerializer,
)
from units.use_cases import UnitListUseCase


class UnitListApi(APIView):

    def get(self, request: Request) -> Response:
        serializer = UnitListInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data
        group_id: int | None = data['group_id']

        units = UnitListUseCase(group_id=group_id).execute()

        serializer = UnitListOutputSerializer(units, many=True)
        return Response({'report_types': serializer.data})
