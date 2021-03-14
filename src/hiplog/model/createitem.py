import datetime

from hiplog.db import save_events
from hiplog.model.projections import existing_ids
from hiplog.model.events import Event, ItemCreatedV1, ItemType


def create_item(
    timestamp: datetime.datetime, type: ItemType, id: str, note, parents: tuple[str]
):
    if not all(parent in existing_ids(until=timestamp) for parent in parents):
        raise InvalidParent(id)

    if id in existing_ids(until=timestamp):
        raise ItemIdExists(id)

    event = Event(
        item_id=id,
        timestamp=timestamp,
        note=note.name,
        payload=ItemCreatedV1(type, parents),
    )
    save_events([event])


class ItemIdExists(Exception):
    def __init__(self, id):
        super().__init__(f"An item with the id {id} is already registered")
        self.id = id


class InvalidParent(Exception):
    def __init__(self, id):
        super().__init__(f"The proposed parents of {id} are invalid")
        self.id = id
