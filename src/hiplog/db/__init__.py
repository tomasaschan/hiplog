import os
import os.path
import pickle

from hiplog.model.events import Event

EVENTS_FILE = "data/events.pickle"


def save_events(events: list[Event]):
    """
    Append events to the database
    """
    if not os.path.exists(os.path.dirname(EVENTS_FILE)):
        os.makedirs(os.path.dirname(EVENTS_FILE))

    with open(EVENTS_FILE, "ba+") as f:
        pickle.dump(events, f)


def read_events():
    """
    Read all events from the database
    """

    # see https://stackoverflow.com/a/12762056/38055
    events = []
    with open(EVENTS_FILE, "rb") as f:
        try:
            while True:
                events.extend(pickle.load(f))
        except (FileNotFoundError, EOFError):
            return events
