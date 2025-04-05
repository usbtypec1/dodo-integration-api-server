from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from telegram.serializers import (
    TelegramChatUpsertInputSerializer,
    TelegramChatUpsertOutputSerializer,
)
from telegram.use_cases import TelegramChatUpsertUseCase


class TelegramChatUpsertApi(APIView):

    def post(self, request: Request) -> Response:
        serializer = TelegramChatUpsertInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        chat_id: int = data["id"]
        title: str = data["title"]
        username: str | None = data["username"]

        chat = TelegramChatUpsertUseCase(
            chat_id=chat_id,
            title=title,
            username=username,
        ).execute()

        serializer = TelegramChatUpsertOutputSerializer(chat)
        return Response(serializer.data, status.HTTP_201_CREATED)
