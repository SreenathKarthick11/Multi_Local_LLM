# ui/clock.py
import time

_start_time = None


def start():
    global _start_time
    _start_time = time.time()


def elapsed():
    if _start_time is None:
        return 0.0
    return time.time() - _start_time