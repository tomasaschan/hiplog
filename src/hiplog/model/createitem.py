import datetime
from enum import auto

from hiplog.model import ParsableEnum


class ItemType(ParsableEnum):
    hips = auto()


def create_item(
    timestamp: datetime.datetime,
    type: ItemType,
    id: str,
    note,
):
    print(type)
    print(id)
    print(timestamp)
    print(note.name)
