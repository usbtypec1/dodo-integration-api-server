from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.authentication import SpecificTokenAuthentication
from telegram.serializers import (
    TelegramUserUpsertInputSerializer,
    TelegramUserUpsertOutputSerializer,
)
from telegram.use_cases import TelegramUserUpsertUseCase


class TelegramUserUpsertApi(APIView):
    authentication_classes = (SpecificTokenAuthentication,)

    def post(self, request: Request) -> Response:
        serializer = TelegramUserUpsertInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data
        user_id: int = data['id']
        full_name: str = data['full_name']
        username: str | None = data['username']

        user = TelegramUserUpsertUseCase(
            user_id=user_id,
            full_name=full_name,
            username=username,
        ).execute()

        serializer = TelegramUserUpsertOutputSerializer(user)
        status_code = (
            status.HTTP_201_CREATED if user.is_created else status.HTTP_200_OK
        )
        return Response(serializer.data, status_code)
