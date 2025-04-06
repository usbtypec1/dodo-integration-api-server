from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import AccountTokenRetrieveOutputSerializer
from accounts.use_cases import AccountTokenRetrieveUseCase


class AccountTokenRetrieveApi(APIView):

    def get(self, request: Request, account_token_id: str) -> Response:
        account_token = AccountTokenRetrieveUseCase(
            account_token_id=account_token_id,
        ).execute()
        serializer = AccountTokenRetrieveOutputSerializer(account_token)
        return Response(serializer.data)
