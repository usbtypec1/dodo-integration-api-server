from collections.abc import Iterable
from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramUserUnitUpdateUseCase:
    user_id: int
    unit_ids: Iterable[UUID]

    def execute(self) -> None:
        pass

