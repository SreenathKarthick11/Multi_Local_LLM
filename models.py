from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    answer: str = Field(description="The final answer")
    confidence: float = Field(description="Confidence score between 0 and 1")
    reasoning: str = Field(description="Reasoning used to reach the answer")

class CritiqueResponse(BaseModel):
    weaknesses: list[str] = Field(description="Weaknesses in the opponent answer")
    hallucination_risk: int = Field(description="Risk score from 1 to 5")
    suspected_hallucinations: list[str] = Field(description="Statements that may be fabricated or unsupported")

class SearchDecision(BaseModel):
    need_search: bool = Field(description="Whether a search is needed")
    confidence: float = Field(description="Confidence score between 0 and 1")
    search_query: str = Field(description="The query to use for searching")
    reason: str = Field(description="The reason for the search decision")

class JudgeResponse(BaseModel):
    winner: str = Field(description="The winner of the debate, either 'A' or 'B'")
    confidence: float = Field(description="Confidence score between 0 and 1")
    reasoning: str = Field(description="Reasoning used to reach the judgment")

class EvaluationResponse(BaseModel):
    correct: bool = Field(description="Whether the final answer is correct")
    score: int = Field(description="Quality score from 1-10")
    reasoning: str = Field(description="Reasoning for the evaluation")

class ToolDecision(BaseModel):
    use_tool: bool = Field(description="Whether another tool should be used.")
    tool_name: str = Field(description="calculator, python, retrieval, none")
    tool_input: str = Field(description="Input for the tool.")
    confidence: float = Field(description="Confidence score between 0 and 1")
    reason: str = Field(description="The reason for the tool decision")

class ToolResult(BaseModel):
    tool_name: str = Field(description="calculator, python, retrieval, none")
    tool_input: str = Field(description="Input for the tool.")
    output: str = Field(description="Output from the tool.")

class ResourceContext(BaseModel):
    web_evidence: str = Field(default="")
    rag_evidence: str = Field(default="")
    tools: list[ToolResult] = Field(default_factory=list)

class ResourceDecision(BaseModel):
    use_rag: bool = Field(description="Whether retrieval from the vector database is useful.")
    retrieval_query: str = Field(description="Query to search the vector database.")
    confidence: float = Field(description="Confidence between 0 and 1.")
    reason: str = Field(description="Reason for the decision.")