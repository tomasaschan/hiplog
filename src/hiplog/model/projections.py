from dataclasses import dataclass, field
import datetime

from hiplog.db import with_events
from hiplog.model.events import ItemCreatedV1


@dataclass
class Item:
    id: str
    created_at: datetime.datetime
    parents: list = field(default_factory=list)
    children: list = field(default_factory=list)


@with_events
def existing_ids(events):
    for event in events:
        if isinstance(event.payload, ItemCreatedV1):
            yield event.item_id


@with_events
def all_items(events) -> dict[str, Item]:
    sorted_events = sorted(events, key=lambda event: event.timestamp)
    items = {}
    for event in sorted_events:
        if isinstance(event.payload, ItemCreatedV1):
            item = Item(event.item_id, event.timestamp)
            for parent in event.payload.parents:
                item.parents.append(items[parent])
                items[parent].children.append(item)
            items[event.item_id] = item
    return items
