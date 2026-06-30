"""
UI State

This file stores ONLY information required for rendering the UI.

It intentionally knows nothing about LangGraph or DebateState.

The debate engine converts its own state into UI events,
which update this state.
"""

from dataclasses import dataclass, field


# -----------------------------------------------------
# Router
# -----------------------------------------------------

@dataclass
class RouterState:

    status: str = "Waiting"

    use_web: bool = False
    use_rag: bool = False
    use_python: bool = False

    confidence: float = 0.0

    reason: str = ""


# -----------------------------------------------------
# Resources
# -----------------------------------------------------

@dataclass
class ResourceState:

    web: str = ""

    rag: str = ""

    tools: str = ""


# -----------------------------------------------------
# Agent
# -----------------------------------------------------

@dataclass
class AgentState:

    status: str = "Idle"

    answer: str = ""

    reasoning: str = ""

    confidence: float = 0.0


# -----------------------------------------------------
# Critique
# -----------------------------------------------------

@dataclass
class CritiqueState:

    weaknesses: list[str] = field(default_factory=list)

    hallucination_risk: int = 0

    hallucinations: list[str] = field(default_factory=list)


# -----------------------------------------------------
# Judge
# -----------------------------------------------------

@dataclass
class JudgeState:

    winner: str = ""

    reasoning: str = ""

    confidence: float = 0.0


# -----------------------------------------------------
# Runtime
# -----------------------------------------------------

@dataclass
class RuntimeState:

    round_number: int = 1

    max_rounds: int = 3

    elapsed_seconds: float = 0.0

    stop_reason: str = ""


# -----------------------------------------------------
# Entire UI
# -----------------------------------------------------

@dataclass
class UIState:

    question: str = ""

    router: RouterState = field(default_factory=RouterState)

    resources: ResourceState = field(default_factory=ResourceState)

    agent_a: AgentState = field(default_factory=AgentState)

    agent_b: AgentState = field(default_factory=AgentState)

    critique_a: CritiqueState = field(default_factory=CritiqueState)

    critique_b: CritiqueState = field(default_factory=CritiqueState)

    judge: JudgeState = field(default_factory=JudgeState)

    runtime: RuntimeState = field(default_factory=RuntimeState)