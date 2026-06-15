from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    answer: str = Field(description="The final answer")
    confidence: float = Field(
        description="Confidence score between 0 and 1"
    )
    reasoning: str = Field(
        description="Reasoning used to reach the answer"
    )