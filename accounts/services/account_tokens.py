from accounts.exceptions import AccountTokenNotFoundError
from accounts.models import AccountTokens


def get_account_tokens_by_id(account_token_id: str) -> AccountTokens:
    try:
        return AccountTokens.objects.get(id=account_token_id)
    except AccountTokens.DoesNotExist:
        raise AccountTokenNotFoundError
