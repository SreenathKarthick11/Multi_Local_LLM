import math


SAFE_GLOBALS = {
    "__builtins__": {},
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "pi": math.pi,
    "e": math.e,
    "pow": pow,
    "abs": abs,
    "round": round,
}


def calculator(expression: str) -> str:
    try:
        result = eval(expression, SAFE_GLOBALS, {})
        return str(result)
    except Exception as e:
        return f"Calculator Error: {e}"