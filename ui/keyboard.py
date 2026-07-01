# ui/keyboard.py
import sys

try:
    import msvcrt
    IS_WINDOWS = True
except ImportError:
    import termios
    import tty
    import select
    IS_WINDOWS = False


def init():
    """Put stdin into raw, no-echo mode. Returns state to restore later (Unix only)."""
    if IS_WINDOWS:
        return None

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    new_settings = termios.tcgetattr(fd)
    new_settings[3] = new_settings[3] & ~(termios.ICANON | termios.ECHO)
    termios.tcsetattr(fd, termios.TCSANOW, new_settings)
    return old_settings


def restore(old_settings):
    if IS_WINDOWS or old_settings is None:
        return
    fd = sys.stdin.fileno()
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def read_key():
    """
    Non-blocking read of one keypress.
    Returns "ENTER", "BACKSPACE", a printable char, or None if nothing waiting.
    """
    if IS_WINDOWS:
        if msvcrt.kbhit():
            ch = msvcrt.getwch()
            if ch in ("\r", "\n"):
                return "ENTER"
            if ch == "\x08":
                return "BACKSPACE"
            if ch.isprintable():
                return ch
            return None
        return None

    dr, _, _ = select.select([sys.stdin], [], [], 0)
    if dr:
        ch = sys.stdin.read(1)
        if ch in ("\r", "\n"):
            return "ENTER"
        if ch in ("\x7f", "\x08"):
            return "BACKSPACE"
        if ch.isprintable():
            return ch
        return None
    return None