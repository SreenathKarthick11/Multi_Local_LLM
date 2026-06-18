from langgraph.graph import StateGraph
from langgraph.graph import START, END

from state import DebateState

from agents.debater_a import debater_a,critique_a,revise_a
from agents.debater_b import debater_b,critique_b,revise_b
from agents.judge import judge


builder = StateGraph(DebateState)

# Mermaid diagram for the graph
#             +-----------+
#             | __start__ |
#             +-----------+
#             ***        ***
#            *              *
#          **                **
# +-----------+           +-----------+
# | debater_b |           | debater_a |
# +-----------+           +-----------+
#        *                      *
#        *                      *
#        *                      *
# +------------+         +------------+
# | critique_a |         | critique_b |
# +------------+         +------------+
#        *                      *
#        *                      *
#        *                      *
#  +----------+           +----------+
#  | revise_a |           | revise_b |
#  +----------+           +----------+
#             ***        ***
#                *      *
#                 **  **
#               +-------+
#               | judge |
#               +-------+
#                   *
#                   *
#                   *
#              +---------+
#              | __end__ |
#              +---------+


builder.add_node("debater_a", debater_a)
builder.add_node("debater_b", debater_b)

builder.add_node("critique_a", critique_a)
builder.add_node("critique_b", critique_b)

builder.add_node("revise_a", revise_a)
builder.add_node("revise_b", revise_b)

builder.add_node("judge", judge)


builder.add_edge(START, "debater_a")
builder.add_edge(START, "debater_b")

builder.add_edge("debater_a", "critique_b")
builder.add_edge("debater_b", "critique_a")

builder.add_edge("critique_a", "revise_a")
builder.add_edge("critique_b", "revise_b")

builder.add_edge("revise_a", "judge")
builder.add_edge("revise_b", "judge")

builder.add_edge("judge", END)

graph = builder.compile()