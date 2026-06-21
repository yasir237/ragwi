from pydantic import BaseModel
from typing import List

class QuestionRequest(BaseModel):
    question: str
    top_k: int = 5

class ChunkResponse(BaseModel):
    id: int
    text: str

class AnswerResponse(BaseModel):
    answer: str
    chunks: List[ChunkResponse]