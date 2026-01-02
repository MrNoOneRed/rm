from typing import Any


def empty_dict_to_none(v: Any) -> Any | None:
    if v == {}:
        return None
    return v