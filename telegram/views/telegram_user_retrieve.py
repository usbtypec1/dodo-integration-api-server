from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from core.authentication import SpecificTokenAuthentication
from telegram.serializers import TelegramUserRetrieveOutputSerializer
from telegram.use_cases import TelegramUserRetrieveUseCase


class TelegramUserRetrieveApi(APIView):
    authentication_classes = (SpecificTokenAuthentication,)

    def get(self, request: Request, user_id: int) -> Response:
        user = TelegramUserRetrieveUseCase(user_id=user_id).execute()
        serializer = TelegramUserRetrieveOutputSerializer(user)
        return Response(serializer.data)
