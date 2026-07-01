# renderer.py

from dataclasses import asdict
from rich.panel import Panel
from rich.text import Text
from ui.state import UIState

from ui.events import (
    QuestionEvent,
    RouterEvent,
    ResourceEvent,
    AgentEvent,
    CritiqueEvent,
    JudgeEvent,
    RuntimeEvent,
)

from ui.layout import build_layout

from ui.panels import (
    render_router,
    render_resources,
    render_debate,
    render_critique_a,
    render_critique_b,
    render_judge,
    render_runtime,
)

from ui.event_bus import event_bus

class Renderer:

    def __init__(self):

        self.state = UIState()

        self.layout = build_layout()

        self.refresh()

    # -----------------------------------------------------
    # Public API
    # -----------------------------------------------------

    def update(self, event):

        if isinstance(event, QuestionEvent):
            self._update_question(event)

        elif isinstance(event, RouterEvent):
            self._update_router(event)

        elif isinstance(event, ResourceEvent):
            self._update_resources(event)

        elif isinstance(event, AgentEvent):
            self._update_agent(event)

        elif isinstance(event, CritiqueEvent):
            self._update_critique(event)

        elif isinstance(event, JudgeEvent):
            self._update_judge(event)

        elif isinstance(event, RuntimeEvent):
            self._update_runtime(event)

        self.refresh()

    # -----------------------------------------------------
    # Refresh Panels
    # -----------------------------------------------------

    def refresh(self):

        self.layout["header"].update(
            Panel(
                Text(
                    self.state.question or "Local LLM Multi-Agent Debate",
                    justify="center",
                    style="title",
                )
            )
        )

        self.layout["router"].update(render_router(self.state))
        self.layout["resources"].update(render_resources(self.state))
        self.layout["debate"].update(render_debate(self.state))
        self.layout["critique_a"].update(render_critique_a(self.state))
        self.layout["critique_b"].update(render_critique_b(self.state))
        self.layout["judge"].update(render_judge(self.state))
        self.layout["runtime"].update(render_runtime(self.state))

        self.layout["footer"].update(
            Text("Press Ctrl+C to exit", justify="center", style="dim")
        )

    # -----------------------------------------------------
    # Individual Event Handlers
    # -----------------------------------------------------

    def _update_question(self, event: QuestionEvent):

        self.state.question = event.question

    def _update_router(self, event: RouterEvent):

        self.state.router.status = event.status
        self.state.router.use_web = event.use_web
        self.state.router.use_rag = event.use_rag
        self.state.router.use_python = event.use_python
        self.state.router.confidence = event.confidence
        self.state.router.reason = event.reason

    def _update_resources(self, event: ResourceEvent):

        self.state.resources.web = event.web
        self.state.resources.rag = event.rag
        self.state.resources.tools = event.tools

    def _update_agent(self, event: AgentEvent):

        if event.agent.upper() == "A":

            agent = self.state.agent_a

        else:

            agent = self.state.agent_b

        agent.status = event.status
        agent.answer = event.answer
        agent.reasoning = event.reasoning
        agent.confidence = event.confidence

    def _update_critique(self, event: CritiqueEvent):

        if event.agent.upper() == "A":

            critique = self.state.critique_a

        else:

            critique = self.state.critique_b

        critique.weaknesses = event.weaknesses
        critique.hallucination_risk = event.hallucination_risk
        critique.hallucinations = event.hallucinations

    def _update_judge(self, event: JudgeEvent):

        self.state.judge.winner = event.winner
        self.state.judge.reasoning = event.reasoning
        self.state.judge.confidence = event.confidence

    def _update_runtime(self, event: RuntimeEvent):

        self.state.runtime.round_number = event.round_number
        self.state.runtime.max_rounds = event.max_rounds
        self.state.runtime.elapsed_seconds = event.elapsed_seconds
        self.state.runtime.stop_reason = event.stop_reason

    def process_events(self):

        events = event_bus.poll()

        for event in events:

            self.update(event)

    # -----------------------------------------------------
    # Helpers
    # -----------------------------------------------------

    def get_layout(self):

        return self.layout

    def get_state(self):

        return self.state

    def reset(self):

        self.state = UIState()

        self.refresh()

    def dump(self):

        return asdict(self.state)