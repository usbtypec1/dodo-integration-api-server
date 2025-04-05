from dataclasses import dataclass

from telegram.services.chats import upsert_telegram_chat


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramChatUpsertResultDto:
    id: int
    title: str | None
    username: str | None
    is_created: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramChatUpsertUseCase:
    chat_id: int
    title: str | None
    username: str | None

    def execute(self) -> TelegramChatUpsertResultDto:
        user, is_created = upsert_telegram_chat(
            chat_id=self.chat_id,
            title=self.title,
            username=self.username,
        )
        return TelegramChatUpsertResultDto(
            id=user.id,
            title=user.title,
            username=user.username,
            is_created=is_created,
        )
