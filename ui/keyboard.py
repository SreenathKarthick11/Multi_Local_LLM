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
    sys.stdout.write("\x1b[?1000h\x1b[?1006h")  # enable SGR mouse reporting
    sys.stdout.flush()

    if IS_WINDOWS:
        return None

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    new_settings = termios.tcgetattr(fd)
    new_settings[3] = new_settings[3] & ~(termios.ICANON | termios.ECHO)
    termios.tcsetattr(fd, termios.TCSANOW, new_settings)
    return old_settings


def restore(old_settings):
    sys.stdout.write("\x1b[?1000l\x1b[?1006l")  # disable mouse reporting
    sys.stdout.flush()

    if IS_WINDOWS or old_settings is None:
        return
    fd = sys.stdin.fileno()
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def _try_read_more(timeout=0.02):
    dr, _, _ = select.select([sys.stdin], [], [], timeout)
    return sys.stdin.read(1) if dr else None


def _parse_sgr_mouse(seq):
    if not seq or seq[-1] not in ("M", "m"):
        return None
    is_press = seq[-1] == "M"
    body = seq[:-1]
    try:
        cb_str, cx_str, cy_str = body.split(";")
        cb, cx, cy = int(cb_str), int(cx_str), int(cy_str)
    except ValueError:
        return None

    if cb == 64:
        return ("SCROLL_UP", cx, cy)
    if cb == 65:
        return ("SCROLL_DOWN", cx, cy)
    if is_press and (cb & 3) == 0:
        return ("CLICK", cx, cy)
    return None


def read_key():
    """
    Returns "ENTER", "BACKSPACE", "UP", "DOWN", a printable char,
    ("CLICK", col, row), ("SCROLL_UP", col, row), ("SCROLL_DOWN", col, row),
    or None.
    """
    if IS_WINDOWS:
        if msvcrt.kbhit():
            ch = msvcrt.getwch()
            if ch in ("\r", "\n"):
                return "ENTER"
            if ch == "\x08":
                return "BACKSPACE"
            if ch == "\xe0":
                ch2 = msvcrt.getwch()
                return {"H": "UP", "P": "DOWN"}.get(ch2)
            if ch.isprintable():
                return ch
        return None

    dr, _, _ = select.select([sys.stdin], [], [], 0)
    if not dr:
        return None

    ch = sys.stdin.read(1)

    if ch == "\x1b":
        ch2 = _try_read_more()
        if ch2 != "[":
            return "ESC"

        ch3 = _try_read_more()
        if ch3 == "A":
            return "UP"
        if ch3 == "B":
            return "DOWN"
        if ch3 == "<":
            seq = ""
            while True:
                c = _try_read_more()
                if c is None:
                    break
                seq += c
                if c in ("M", "m"):
                    break
            return _parse_sgr_mouse(seq)
        return "ESC"

    if ch in ("\r", "\n"):
        return "ENTER"
    if ch in ("\x7f", "\x08"):
        return "BACKSPACE"
    if ch.isprintable():
        return ch
    return None