from langgraph.graph import StateGraph
from langgraph.graph import START, END

from state import DebateState

from agents.debater_a import debater_a,critique_a,revise_a
from agents.debater_b import debater_b,critique_b,revise_b
from agents.judge import judge
from agents.debate_controller import debate_controller, should_continue,pass_through


builder = StateGraph(DebateState)


# ----------------------------
# Nodes
# ----------------------------

builder.add_node("debater_a", debater_a)
builder.add_node("debater_b", debater_b)

builder.add_node("critique_a", critique_a)
builder.add_node("critique_b", critique_b)

builder.add_node("revise_a", revise_a)
builder.add_node("revise_b", revise_b)

builder.add_node("sync", pass_through)
builder.add_node("controller",debate_controller)
builder.add_node("round_start",pass_through)
builder.add_node("judge", judge)

# Initial Answer Generation
builder.add_edge(START,"debater_a")
builder.add_edge(START,"debater_b")

# First Critique Round
builder.add_edge("debater_a","critique_b")
builder.add_edge("debater_b","critique_a")

# Revision Round
builder.add_edge("critique_a","revise_a")
builder.add_edge("critique_b","revise_b")

# Synchronization Barrier
builder.add_edge("revise_a","sync")
builder.add_edge("revise_b","sync")

# Debate Controller
builder.add_edge("sync","controller")

# Continue Debate or Judge
builder.add_conditional_edges(
    "controller",
    should_continue,
    {
        "continue": "round_start",
        "judge": "judge",
    }
)

# Start Next Debate Round
builder.add_edge("round_start","critique_a")
builder.add_edge("round_start","critique_b")

# End Debate
builder.add_edge("judge",END)

graph = builder.compile()