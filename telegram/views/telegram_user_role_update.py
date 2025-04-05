from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from telegram.serializers import TelegramUserRoleUpdateInputSerializer
from telegram.use_cases import TelegramUserRoleUpdateUseCase


class TelegramUserRoleUpdateApi(APIView):

    def patch(self, request: Request, user_id: int) -> Response:
        serializer = TelegramUserRoleUpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data: dict = serializer.validated_data
        access_code: str = data['access_code']

        TelegramUserRoleUpdateUseCase(
            user_id=user_id,
            access_code=access_code,
        ).execute()

        return Response(status=status.HTTP_204_NO_CONTENT)
