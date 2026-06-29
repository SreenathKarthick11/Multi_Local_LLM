import math
import statistics
import random

SAFE_GLOBALS = {
    "__builtins__": {},

    # math
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,

    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,

    "ceil": math.ceil,
    "floor": math.floor,
    "fabs": math.fabs,

    "factorial": math.factorial,
    "gcd": math.gcd,
    "lcm": math.lcm,

    "pi": math.pi,
    "e": math.e,

    # builtins
    "abs": abs,
    "round": round,
    "min": min,
    "max": max,
    "sum": sum,
    "len": len,
    "pow": pow,

    # statistics
    "mean": statistics.mean,
    "median": statistics.median,
    "mode": statistics.mode,
    "stdev": statistics.stdev,
    "variance": statistics.variance,
    "pstdev": statistics.pstdev,
    "pvariance": statistics.pvariance,

    # random (optional)
    "randint": random.randint,
}

def normalize(expr: str):

    expr = expr.replace("^", "**")
    expr = expr.replace("×", "*")
    expr = expr.replace("÷", "/")
    expr = expr.replace("π", "pi")

    return expr

def python_tool(code: str) -> str:
    """
    Executes a single safe Python expression.

    Example:
        mean([1,2,3])
        sqrt(25)
        factorial(8)
        variance([1,2,3,4])
    """
    code = normalize(code)
    
    try:
        result = eval(code, SAFE_GLOBALS, {})
        return str(result)

    except Exception as e:
        return f"Python Tool Error: {e}"