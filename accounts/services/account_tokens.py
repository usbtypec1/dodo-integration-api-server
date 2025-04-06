import httpx
from django.conf import settings

from accounts.exceptions import AccountTokenNotFoundError
from accounts.models import AccountTokens
from accounts.services.encryption import decrypt_string, encrypt_string


def get_account_tokens_by_id(account_token_id: str) -> AccountTokens:
    try:
        return AccountTokens.objects.get(id=account_token_id)
    except AccountTokens.DoesNotExist:
        raise AccountTokenNotFoundError


def update_account_tokens(account_tokens: AccountTokens) -> None:
    refresh_token = decrypt_string(account_tokens.encrypted_refresh_token)

    url = 'https://auth.dodois.io/connect/token'
    request_data = {
        'client_id': settings.DODO_IS_API_CLIENT_ID,
        'client_secret': settings.DODO_IS_API_CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
    }
    with httpx.Client() as http_client:
        response = http_client.post(url, data=request_data)

    response_data = response.json()

    plain_access_token: str = response_data['access_token']
    plain_refresh_token: str = response_data['refresh_token']

    account_tokens.encrypted_access_token = encrypt_string(
        plain_access_token,
    )
    account_tokens.encrypted_refresh_token = encrypt_string(
        plain_refresh_token,
    )
    account_tokens.save(
        update_fields=(
            'encrypted_access_token',
            'encrypted_refresh_token',
            'updated_at',
        )
    )
