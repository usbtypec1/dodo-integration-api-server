from dataclasses import dataclass
from uuid import UUID

from units.models import Unit


@dataclass(frozen=True, slots=True, kw_only=True)
class UnitListItemDto:
    id: UUID
    name: str
    legacy_id: int
    group_id: int
    group_name: str
    office_manager_account_id: str | None
    shift_manager_account_id: str | None
    dodo_is_api_account_id: str | None


def get_units(*, group_id: int | None) -> list[UnitListItemDto]:
    units = (
        Unit.objects
        .select_related(
            'group',
            'dodo_is_api_account_tokens',
            'office_manager_account_cookies',
            'shift_manager_account_cookies',
        )
    )
    if group_id is not None:
        units = units.filter(group_id=group_id)

    result: list[UnitListItemDto] = []

    for unit in units:
        office_manager_account_id = None
        if unit.office_manager_account_cookies is not None:
            office_manager_account_id = (
                unit.office_manager_account_cookies.account_id
            )

        shift_manager_account_id = None
        if unit.shift_manager_account_cookies is not None:
            shift_manager_account_id = (
                unit.shift_manager_account_cookies.account_id
            )

        dodo_is_api_account_id = None
        if unit.dodo_is_api_account_tokens is not None:
            dodo_is_api_account_id = (
                unit.dodo_is_api_account_tokens.account_id
            )

        unit_list_item = UnitListItemDto(
            id=unit.id,
            name=unit.name,
            legacy_id=unit.legacy_id,
            group_id=unit.group.id,
            group_name=unit.group.name,
            office_manager_account_id=office_manager_account_id,
            shift_manager_account_id=shift_manager_account_id,
            dodo_is_api_account_id=dodo_is_api_account_id,
        )
        result.append(unit_list_item)

    return result
