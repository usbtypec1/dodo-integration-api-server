from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.authentication import SpecificTokenAuthentication
from reports.serializers import (
    ReportRouteCreateInputSerializer,
    ReportRouteDeleteInputSerializer,
    ReportRouteListInputSerializer,
    ReportRouteListOutputSerializer,
)
from reports.use_cases import (
    ReportRouteCreateUseCase,
    ReportRouteDeleteUseCase,
    ReportRouteListUseCase,
)


class ReportRouteListCreateDeleteApi(APIView):
    authentication_classes = (SpecificTokenAuthentication,)

    def get(self, request: Request) -> Response:
        serializer = ReportRouteListInputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data
        report_type_id: str | None = data["report_type_id"]
        unit_id: int | None = data["unit_id"]
        chat_ids: list[int] | None = data["chat_ids"]
        take: int = data["take"]
        skip: int = data["skip"]

        report_routes = ReportRouteListUseCase(
            report_type_id=report_type_id,
            unit_id=unit_id,
            chat_ids=chat_ids,
            take=take,
            skip=skip,
        ).execute()

        serializer = ReportRouteListOutputSerializer(report_routes)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = ReportRouteCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data
        report_type_id: str = data["report_type_id"]
        unit_legacy_id: int = data["unit_legacy_id"]
        chat_id: int = data["chat_id"]

        ReportRouteCreateUseCase(
            report_type_id=report_type_id,
            unit_legacy_id=unit_legacy_id,
            chat_id=chat_id,
        ).execute()

        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request: Request) -> Response:
        serializer = ReportRouteDeleteInputSerializer(
            data=request.query_params,
        )
        serializer.is_valid(raise_exception=True)

        data: dict = serializer.validated_data
        report_type_id: str = data["report_type_id"]
        unit_legacy_id: int = data["unit_legacy_id"]
        chat_id: int = data["chat_id"]

        ReportRouteDeleteUseCase(
            report_type_id=report_type_id,
            unit_legacy_id=unit_legacy_id,
            chat_id=chat_id,
        ).execute()

        return Response(status=status.HTTP_204_NO_CONTENT)
