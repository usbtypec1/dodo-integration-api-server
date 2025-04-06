from dataclasses import dataclass

from accounts.services.account_tokens import get_account_tokens_by_id
from accounts.services.encryption import decrypt_string


@dataclass(frozen=True, slots=True, kw_only=True)
class AccountTokenRetrieveResultDto:
    account_id: str
    access_token: str


@dataclass(frozen=True, slots=True, kw_only=True)
class AccountTokenRetrieveUseCase:
    account_token_id: str

    def execute(self) -> AccountTokenRetrieveResultDto:
        account_tokens = get_account_tokens_by_id(self.account_token_id)
        access_token = decrypt_string(account_tokens.encrypted_access_token)
        return AccountTokenRetrieveResultDto(
            account_id=account_tokens.id,
            access_token=access_token,
        )
