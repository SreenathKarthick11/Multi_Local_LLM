from llm import tool_llm

from models import ToolResult

from tools.calculator import calculator


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
calculator

Your job is NOT to answer the question.

Your ONLY job is to decide whether a tool should be used.

Use the calculator whenever the question involves ANY numerical computation.

Examples that MUST use calculator:
- 2+2
- 19*48
- sqrt(81)
- 18/7
- 15% of 230
- 2^15
- factorial of 8
- convert 5 miles to km (if calculator supports it)
- average of 5,7,10
- compound interest
- any arithmetic expression

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
tool_name: calculator
tool_input: ONLY the mathematical expression.

"""
    )

    if not decision.use_tool:
        return None

    if decision.tool_name == "calculator":

        output = calculator(
            decision.tool_input
        )

        return ToolResult(
            tool_name="calculator",
            tool_input=decision.tool_input,
            output=output,
        )

    return None