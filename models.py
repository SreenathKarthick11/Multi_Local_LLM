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