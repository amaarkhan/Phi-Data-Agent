# schema.py
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

class InterestInput(BaseModel):
    interest: str = Field(..., min_length=3, description="User's topic of interest for book recommendations")

class BookRecommendation(BaseModel):
    title: str
    author: str
    description: str
