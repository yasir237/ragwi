from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models.BaseDataModel import get_db
from controllers.NLPController import NLPController
from routes.schemes.nlp import QuestionRequest, AnswerResponse

router = APIRouter(prefix="/api/v1/nlp")

@router.post("/project/{project_id}/ask", response_model=AnswerResponse)
async def ask_question(
    project_id: int,
    request: QuestionRequest,
    db: AsyncSession = Depends(get_db)
):
    controller = NLPController(db)
    result = await controller.answer_question(
        question=request.question,
        project_id=project_id,
        top_k=request.top_k
    )
    return result