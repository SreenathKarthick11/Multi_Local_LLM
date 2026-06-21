from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    answer: str = Field(description="The final answer")
    confidence: float = Field(description="Confidence score between 0 and 1")
    reasoning: str = Field(description="Reasoning used to reach the answer")

class CritiqueResponse(BaseModel):
    weaknesses: list[str] = Field(description="Weaknesses in the opponent answer")
    hallucination_risk: int = Field(description="Risk score from 1 to 5")
    suspected_hallucinations: list[str] = Field(description="Statements that may be fabricated or unsupported")