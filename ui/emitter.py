# emitter.py

from ui.event_bus import event_bus


def emit(event):

    event_bus.emit(event)