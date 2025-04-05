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
