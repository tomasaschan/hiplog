import dataclasses
import datetime
import enum
import ndjson
import os
import os.path
import uuid

from hiplog.model.events import Event

EVENTS_FILE = "data/events.ndjson"


def datetime_aware_converter(value):
    if isinstance(value, datetime.datetime):
        return value.isoformat()
    if isinstance(value, uuid.UUID):
        return str(value)
    if isinstance(value, enum.Enum):
        return str(value)


def save_events(events: list[Event]):
    if not os.path.exists(os.path.dirname(EVENTS_FILE)):
        os.makedirs(os.path.dirname(EVENTS_FILE))

    with open(EVENTS_FILE, "a") as f:
        writer = ndjson.writer(f, default=datetime_aware_converter)
        for event in events:
            writer.writerow(
                {
                    **dataclasses.asdict(event),
                    "type": type(event.payload).__name__,
                }
            )
