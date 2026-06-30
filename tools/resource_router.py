from llm import resource_router_llm
from models import ResourceRoute


COMMANDS = {
    "@web": "web",
    "@file": "rag",
    "@python": "python",
}


def _extract_commands(question: str):
    """
    Extract explicit routing commands.

    Supported:
        @web
        @file
        @python
    """

    lower = question.lower()

    force_web = "@web" in lower
    force_rag = "@file" in lower
    force_python = "@python" in lower

    cleaned = (
        question.replace("@web", "")
        .replace("@file", "")
        .replace("@python", "")
        .strip()
    )

    return cleaned, force_web, force_rag, force_python


def route_resources(question: str) -> ResourceRoute:
    """
    Decide which resources are required.

    Explicit commands override the LLM:

        @web
        @file
        @python
    """

    question, force_web, force_rag, force_python = _extract_commands(question)

    prompt = f"""
You are a routing agent.

Your ONLY job is deciding which resources are needed.

Never answer the question.

Question:
{question}

Resources
---------

1. Web Search

Use when information requires

- current events
- recent information
- news
- people
- companies
- history
- geography
- scientific facts
- statistics
- information not contained in local files


2. Local RAG

Use when the question depends on uploaded files.

Examples

- my CV
- my resume
- uploaded document
- uploaded PDF
- this paper
- my notes
- my report
- my thesis
- my project

If uploaded documents are enough,
DO NOT use web.


3. Python Tool

Use only for numerical computation.

Examples

- arithmetic
- percentages
- statistics
- averages
- factorial
- logarithms
- trigonometry
- mathematical expressions

Never use Python for factual questions.


Priority

Uploaded files
    >
Web Search

Meaning:

If the answer can be obtained entirely from uploaded
documents,

use_rag=true

use_web=false


Return ONLY

use_web
web_query

use_rag
rag_query

use_tool
tool_name
tool_input

confidence
reason
"""

    route = resource_router_llm.invoke(prompt)

    # -------------------------------------------------
    # Explicit command overrides
    # -------------------------------------------------

    if force_web:
        route.use_web = True

    if force_rag:
        route.use_rag = True

    if force_python:
        route.use_tool = True
        route.tool_name = "python"

    # -------------------------------------------------
    # Generate default queries if missing
    # -------------------------------------------------

    if route.use_web and not route.web_query:
        route.web_query = question

    if route.use_rag and not route.rag_query:
        route.rag_query = question

    if route.use_tool and not route.tool_input:
        route.tool_input = question

    return route