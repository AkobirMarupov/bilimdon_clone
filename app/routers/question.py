from fastapi import APIRouter, HTTPException

from app.dependices import db_dep, current_user_dep
from app.models import Question
from app.schemas.question import QuestionResponse, QuestionCreate, QuestionUpdate


router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("/", response_model=list[QuestionResponse])
async def get_questions(session: db_dep):
    return session.query(Question).all()


@router.get("/{question_id}", response_model=QuestionResponse)
async def get_question(question_id: int, session: db_dep):
    question = session.query(Question).filter(Question.id == question_id).first()

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found."
        )

    return question


@router.post("/create/", response_model=QuestionResponse)
async def create_question(
        question: QuestionCreate,
        session: db_dep,
        current_user: current_user_dep
    ):
    db_question = Question(**question.model_dump(), owner_id= current_user.id)

    session.add(db_question)
    session.commit()
    session.refresh(db_question)

    return db_question


@router.put("/update/{question_id}", response_model=QuestionResponse)
async def update_question(
        question_id: int,
        question: QuestionUpdate,
        session: db_dep
    ):
    db_question = session.query(Question).filter(Question.id == question_id).first()

    if not db_question:
        raise HTTPException(
            status_code=404,
            detail="Question not found."
        )

    db_question.title = question.title if question.title else db_question.title
    db_question.description = question.description if question.description else db_question.description
    db_question.topic_id = question.topic_id if question.topic_id else db_question.topic_id

    session.commit()
    session.refresh(db_question)

    return db_question


@router.delete("/delete/{question_id}")
async def delete_question(question_id: int, session: db_dep):
    db_question = session.query(Question).filter(Question.id == question_id).first()

    if not db_question:
        raise HTTPException(
            status_code=404,
            detail="Question not found."
        )

    session.delete(db_question)
    session.commit()

    return {
        "question_id": id,
        "message": "Question deleted."
    }