import datetime

from dataclasses import dataclass
from enum import Enum


class EventType(Enum):
    CREATED = "created"


@dataclass
class Event:
    type: EventType
    date: datetime.datetime
    title: str
    documentation: str
