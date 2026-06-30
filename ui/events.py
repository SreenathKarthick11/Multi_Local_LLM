"""
UI Events

The debate engine emits these.

The renderer consumes these.

The renderer updates UIState.

This keeps the UI completely independent from LangGraph.
"""

from dataclasses import dataclass


# ----------------------------------------------------
# Question
# ----------------------------------------------------

@dataclass
class QuestionEvent:

    question: str


# ----------------------------------------------------
# Router
# ----------------------------------------------------

@dataclass
class RouterEvent:

    status: str

    use_web: bool

    use_rag: bool

    use_python: bool

    confidence: float

    reason: str


# ----------------------------------------------------
# Resources
# ----------------------------------------------------

@dataclass
class ResourceEvent:

    web: str = ""

    rag: str = ""

    tools: str = ""


# ----------------------------------------------------
# Agent
# ----------------------------------------------------

@dataclass
class AgentEvent:

    agent: str

    status: str

    answer: str

    reasoning: str

    confidence: float


# ----------------------------------------------------
# Critique
# ----------------------------------------------------

@dataclass
class CritiqueEvent:

    agent: str

    weaknesses: list[str]

    hallucination_risk: int

    hallucinations: list[str]


# ----------------------------------------------------
# Judge
# ----------------------------------------------------

@dataclass
class JudgeEvent:

    winner: str

    reasoning: str

    confidence: float


# ----------------------------------------------------
# Runtime
# ----------------------------------------------------

@dataclass
class RuntimeEvent:

    round_number: int

    max_rounds: int

    elapsed_seconds: float

    stop_reason: str = ""