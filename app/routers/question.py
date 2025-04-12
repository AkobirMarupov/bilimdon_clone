from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timezone

from app.database import SessionLocal
from app.schemas.user_schema import QuestionCreateModel, QuestionUpdateModel, QuestionResponseModel
from app.models import User, Question, Topic
from app.dependices import db_dep, get_db


qustion_router = APIRouter(
    prefix= '/questions',
    tags= ['Questions']
)


@qustion_router.get('/', response_model= list[QuestionResponseModel])
async def get_question(session: db_dep):
    return session.query(Question).all()



@qustion_router.post('/', response_model= QuestionResponseModel)
async def create_question(question: QuestionCreateModel, session: User = Depends(get_db)):

    db_topic = session.query(Topic).filter(Topic.id == question.topic_id).first()

    if not db_topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    
    db_question = Question(
        owner_id=get_db.id,
        title=question.title,
        description=question.description,
        topic_id=question.topic_id
    )
    session.add(db_question)
    session.commit()
    session.refresh(db_question)

    return db_question


@qustion_router.get('/{question_id}', response_model= QuestionResponseModel)
async def read_question(question_id: int, session: User = Depends(get_db)):

    db_question = session.query(Question).filter(Question.id == question_id).first()

    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    return db_question

@qustion_router.get('/', response_model= list[QuestionResponseModel])
async def read_questions(
    session: User = Depends(get_db),
    skip: int = 0,
    limit: int = 30
):
    questions = session.query(Question).filter(Question.owner_id == get_db.id).offset(skip).limit(limit).all()
    return questions


@qustion_router.put('/{question_id}', response_model= QuestionResponseModel)
async def update_question(question_id: int, question: QuestionUpdateModel,session: User = Depends(get_db)):

    db_question = session.query(Question).filter(Question.id == question_id, Question.owner_id == get_db.id).first()

    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found or you don't have permission")

    if question.title:
        db_question.title = question.title

    if question.description is not None:
        db_question.description = question.description

    if question.topic_id:
        db_topic = session.query(Topic).filter(Topic.id == question.topic_id).first()

        if not db_topic:
            raise HTTPException(status_code=404, detail="Topic not found")

        db_question.topic_id = question.topic_id

    db_question.updated_at = datetime.now(timezone.utc)
    session.commit()
    session.refresh(db_question)

    return db_question


@qustion_router.delete('/{question_id}', response_model= QuestionResponseModel)
async def delete_question(question_id: int, session: User = Depends(get_db)):

    db_question = session.query(Question).filter(Question.id == question_id, Question.owner_id == get_db.id).first()

    if not db_question:
        raise HTTPException(status_code= 404, detail= "Bunday id dagi savol topilmadi")

    session.delete(db_question)
    session.commit()

    return db_question