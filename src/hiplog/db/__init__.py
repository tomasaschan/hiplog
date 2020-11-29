import functools
import os
import os.path
import pickle

from typing import Iterable

from hiplog.model.events import Event

EVENTS_FILE = "data/events.pickle"


def save_events(events: list[Event]):
    """
    Append events to the database
    """
    if not os.path.exists(os.path.dirname(EVENTS_FILE)):
        os.makedirs(os.path.dirname(EVENTS_FILE))

    with open(os.path.realpath(EVENTS_FILE), "ab") as f:
        pickle.dump(events, f)


def with_events(fn):
    @functools.wraps(fn)
    def wrapped(*args, **kwds):
        events = read_events()
        return fn(*args, events=events, **kwds)

    return wrapped


@functools.cache
def read_events():
    return list(read_events_from_disk())


def read_events_from_disk() -> Iterable[Event]:
    """
    Read all events from the database
    """

    # see https://stackoverflow.com/a/12762056/38055
    try:
        with open(EVENTS_FILE, "rb") as f:
            while True:
                yield from pickle.load(f)
    except (PermissionError, FileNotFoundError, EOFError):
        return
