from llm import resource_router_llm
from models import ResourceRoute


def route_resources(question: str) -> ResourceRoute:
    """
    Decide which resources are required to answer the question.

    The router DOES NOT answer the question.
    It only decides whether to use:

    - Web Search
    - Local RAG
    - Python Tool
    """

    prompt = f"""
You are a resource routing agent.

Question:
{question}

Your ONLY job is deciding which resources are needed.

Available resources
-------------------

1. Web Search

Use when information is:

- current
- factual
- historical
- geographical
- company information
- scientific facts
- statistics
- news
- anything not guaranteed to be in local documents


2. Local RAG

Use whenever the user refers to:

- my CV
- my resume
- uploaded documents
- uploaded PDF
- this paper
- my paper
- my notes
- my report
- my thesis
- my project
- documents folder

or whenever the answer depends on local files.


3. Python Tool

Use whenever numerical computation is required.

Examples

- arithmetic
- statistics
- averages
- percentages
- standard deviation
- factorial
- logarithms
- trigonometry
- unit conversions
- mathematical expressions


Rules
-----

Multiple resources may be required.

Examples

Question:
Compare my CV with the average salary of ML Engineers.

Answer:

use_rag = true
use_web = true
use_tool = false


Question:
What is 18*94?

Answer

use_tool = true


Question:
Summarize my uploaded paper.

Answer

use_rag = true


Question:
Latest Nvidia stock price

Answer

use_web = true


Return ONLY:

- use_web
- web_query

- use_rag
- rag_query

- use_tool
- tool_name
- tool_input

- confidence
- reason
"""

    return resource_router_llm.invoke(prompt)