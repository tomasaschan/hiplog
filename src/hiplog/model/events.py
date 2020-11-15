import datetime

from dataclasses import dataclass, field
from typing import Any
from uuid import UUID, uuid4


@dataclass
class Event:
    item_id: str
    timestamp: datetime.datetime
    note: str
    payload: Any
    id: UUID = field(default_factory=uuid4)
