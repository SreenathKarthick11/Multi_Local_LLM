from queue import Queue
from typing import Any


class EventBus:

    def __init__(self):

        self.queue = Queue()

    def emit(self, event: Any):

        self.queue.put(event)

    def poll(self):

        events = []

        while not self.queue.empty():
            events.append(self.queue.get())

        return events


event_bus = EventBus()