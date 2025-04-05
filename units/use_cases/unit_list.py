from dataclasses import dataclass

from units.services.units import get_units, UnitListItemDto


@dataclass(frozen=True, slots=True, kw_only=True)
class UnitListUseCase:
    group_id: int | None

    def execute(self) -> list[UnitListItemDto]:
        return get_units(group_id=self.group_id)
