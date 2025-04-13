from fastapi import APIRouter, HTTPException

from app.dependices import db_dep, current_user_dep
from app.models import Option, Question, Topic
from app.schemas.option import  OptionCreate, OptionUpdate, OptionResponse
from app.schemas.topic import TopicResponse, TopicCreate

router = APIRouter(
    prefix= '/Topic',
    tags= ['topic']
)

@router.post('/create', response_model= TopicResponse)
async def topic_create(topic: TopicCreate, session: db_dep, current_user: current_user_dep):

    topic_creat = session.query(Topic).filter(Topic.id == topic.id).first()

    if not topic_creat:
        raise HTTPException( status_code=404, detail="Topic not found.")

    session.add(topic_creat)
    session.commit()
    session.refresh(topic_creat)

    return topic_creat


@router.delete('/{topic_id}')
async def topic_delete(topic_id: int, session: db_dep, current_user: current_user_dep):

    db_delete = session.query(Topic).first(Topic.id == topic_id).first()

    if not db_delete:
        raise HTTPException(status_code=404, detail="Topic not found.")

    session.delete(db_delete)
    session.commit()

    return db_delete
