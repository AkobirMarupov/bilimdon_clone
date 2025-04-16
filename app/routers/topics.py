from fastapi import APIRouter, HTTPException

from app.dependices import db_dep, admin_user_dep, current_user_dep
from app.models.topic import Topic
from app.models.participation import Participation
from app.schemas.topic import TopicResponse, TopicCreate


router = APIRouter(
    prefix= '/Topic',
    tags= ['topic']
)

@router.get('/', response_model=list[TopicResponse])
async def get_topic(session: db_dep):
    return session.query(Topic).all()


@router.post('/create', response_model= TopicResponse)
async def topic_create(topic: TopicCreate, session: db_dep, current_user:current_user_dep):

    topic_creat = session.query(Topic).filter(Topic.name == topic.name).first()

    if not topic_creat:
        raise HTTPException( status_code=404, detail="Bunday topik mavjud emas yoki allaqachon mavjud.")

    db_topic = Topic(
        name=topic.name
    )

    session.add(topic_creat)
    session.commit()
    session.refresh(topic_creat)

    return db_topic



@router.delete('/{topic_id}')
async def topic_delete(topic_id: int, session: db_dep, admin_user: admin_user_dep):

    db_delete = session.query(Topic).first(Topic.id == topic_id).first()

    if not db_delete:
        raise HTTPException(status_code=404, detail="Topic not found.")

    session.delete(db_delete)
    session.commit()

    return {
        "topic_id": id,
        "message": "Topic deleted."
    }
