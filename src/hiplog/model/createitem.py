from dataclasses import dataclass
import datetime

from hiplog.db import save_events
from hiplog.model.projections import existing_ids
from hiplog.model.events import Event, ItemCreatedV1, ItemType


def create_item(
    timestamp: datetime.datetime,
    type: ItemType,
    id: str,
    note,
):
    if id in existing_ids():
        raise ItemIdExists(id)

    event = Event(
        item_id=id,
        timestamp=timestamp,
        note=note.name,
        payload=ItemCreatedV1(type),
    )
    save_events([event])

class ItemIdExists(Exception):
    def __init__(self, id):
        super().__init__(f"An item with the id {id} is already registered")
        self.id = id