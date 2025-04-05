from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class TelegramChatUpsertApi(APIView):

    def post(self, request: Request) -> Response:
        return Response()
