from pydantic import BaseModel, Field

class UseCaseInput(BaseModel):
    use_case: str = Field(..., description="The use case for which LLM is needed")

class LLMRecommendation(BaseModel):
    model_name: str
    provider: str
    description: str
