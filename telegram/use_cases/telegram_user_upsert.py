from dataclasses import dataclass

from telegram.services.users import upsert_telegram_user


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramUserUpsertResultDto:
    id: int
    full_name: str
    username: str
    is_created: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramUserUpsertUseCase:
    user_id: int
    full_name: str
    username: str | None

    def execute(self) -> TelegramUserUpsertResultDto:
        user, is_created = upsert_telegram_user(
            user_id=self.user_id,
            full_name=self.full_name,
            username=self.username,
        )
        return TelegramUserUpsertResultDto(
            id=user.id,
            full_name=user.full_name,
            username=user.username,
            is_created=is_created,
        )
