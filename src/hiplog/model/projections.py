from hiplog.db import with_events
from hiplog.model.events import ItemCreatedV1


@with_events
def existing_ids(events):
    for event in events:
        if isinstance(event.payload, ItemCreatedV1):
            yield event.item_id
