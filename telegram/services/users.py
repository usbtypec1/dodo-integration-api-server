from telegram.exceptions import UserNotFoundError
from telegram.models import TelegramUser


def get_telegram_user_by_id(user_id: int) -> TelegramUser:
    try:
        return TelegramUser.objects.select_related('role').get(id=user_id)
    except TelegramUser.DoesNotExist:
        raise UserNotFoundError


def upsert_telegram_user(
        *,
        user_id: int,
        full_name: str,
        username: str | None,
) -> tuple[TelegramUser, bool]:
    return TelegramUser.objects.update_or_create(
        id=user_id,
        defaults={
            'full_name': full_name,
            'username': username,
        }
    )
