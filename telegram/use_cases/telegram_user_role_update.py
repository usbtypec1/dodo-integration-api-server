from dataclasses import dataclass

from telegram.services.users import get_telegram_user_by_id
from user_roles.services import get_user_role_by_access_code


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramUserRoleUpdateUseCase:
    user_id: int
    access_code: str

    def execute(self) -> None:
        user = get_telegram_user_by_id(self.user_id)
        role = get_user_role_by_access_code(self.access_code)
        user.role = role
        user.save(update_fields=('role', 'updated_at'))
