import datetime

from dataclasses import dataclass, field
from enum import auto
from typing import Any
from uuid import UUID, uuid4

from hiplog.model import ParsableEnum


class ItemType(ParsableEnum):
    hips = auto()


@dataclass
class ItemCreatedV1:
    type: ItemType
    parents: tuple[str]


@dataclass
class Event:
    item_id: str
    timestamp: datetime.datetime
    note: str
    payload: Any
    id: UUID = field(default_factory=uuid4)
