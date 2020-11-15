from dataclasses import dataclass
import datetime
from enum import auto

from hiplog.db import save_events
from hiplog.model import ParsableEnum
from hiplog.model.events import Event


class ItemType(ParsableEnum):
    hips = auto()


@dataclass
class ItemCreatedV1:
    type: ItemType


def create_item(
    timestamp: datetime.datetime,
    type: ItemType,
    id: str,
    note,
):
    event = Event(
        item_id=id,
        timestamp=timestamp,
        note=note.name,
        payload=ItemCreatedV1(type),
    )
    save_events([event])
