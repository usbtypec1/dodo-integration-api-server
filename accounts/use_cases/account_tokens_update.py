from accounts.models import AccountTokens
from accounts.services.account_tokens import update_account_tokens


class AccountTokensUpdateUseCase:

    def execute(self) -> None:
        for account_tokens in AccountTokens.objects.all():
            update_account_tokens(account_tokens)
