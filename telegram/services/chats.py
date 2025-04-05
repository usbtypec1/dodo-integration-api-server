from telegram.exceptions import TelegramChatNotFoundError
from telegram.models import TelegramChat


def get_telegram_chat_by_id(chat_id: int) -> TelegramChat:
    """
    Get a Telegram chat by its ID.

    Args:
        chat_id (int): The ID of the Telegram chat.

    Returns:
        TelegramChat: The Telegram chat object.

    Raises:
        TelegramChatNotFoundError: If the chat with the given ID does not
        exist.
    """
    try:
        return TelegramChat.objects.get(id=chat_id)
    except TelegramChat.DoesNotExist:
        raise TelegramChatNotFoundError


def upsert_telegram_chat(
        *,
        chat_id: int,
        title: str | None,
        username: str | None,
) -> tuple[TelegramChat, bool]:
    return TelegramChat.objects.update_or_create(
        id=chat_id,
        defaults={
            'title': title,
            'username': username,
        }
    )
