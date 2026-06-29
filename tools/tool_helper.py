from llm import tool_llm

from models import ToolResult

from tools.python_tool import python_tool


def get_tool(question: str):

    decision = tool_llm.invoke(
        f"""
Question:
{question}

You are a tool routing agent.

Question:
{question}

Available Tools
---------------
python

Your job is NOT to answer the question.

Your ONLY job is to decide whether a tool should be used.

If the question is about documents,
resumes,
papers,
facts,
retrieval,

DO NOT use python.

Use the calculator whenever the question involves ANY numerical computation.


The python tool evaluates safe Python expressions.

Available functions include:

Math:
sqrt
sin
cos
tan
asin
acos
atan
log
log10
exp
factorial
gcd
lcm
ceil
floor

Statistics:
mean
median
mode
variance
stdev
pstdev
pvariance

General:
sum
min
max
len
round
abs
pow

Constants:
pi
e

The tool accepts ONE valid Python expression.

Return ONLY the expression.

Do NOT use calculator for:
- history
- geography
- programming
- definitions
- opinions
- reasoning questions
- factual lookup

Return:

use_tool: true or false

If true:
tool_name: python
tool_input: ONE valid Python expression.

"""
    )

    if not decision.use_tool:
        return None

    if decision.tool_name == "python":

        output = python_tool(
            decision.tool_input
        )

        return ToolResult(
            tool_name="python",
            tool_input=decision.tool_input,
            output=output,
        )

    return None