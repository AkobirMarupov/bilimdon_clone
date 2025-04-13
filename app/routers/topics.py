from fastapi import APIRouter, HTTPException, Depends

from app.dependices import db_dep, current_user_dep
from app.models.topic import Topic
from app.models.participation import Participation
from app.schemas.topic import TopicResponse, TopicCreate
from app.models.user import User

router = APIRouter(
    prefix= '/Topic',
    tags= ['topic']
)

@router.post('/create', response_model= TopicResponse)
async def topic_create(topic: TopicCreate, session: db_dep, current_user: User = Depends(current_user_dep)):

    topic_creat = session.query(Topic).filter(Topic.name == topic.name).first()

    if not topic_creat:
        raise HTTPException( status_code=404, detail="Bunday topik mavjud emas yoki allaqachon mavjud.")

    db_topic = Topic(name=topic.name)
    session.add(topic_creat)
    session.commit()
    session.refresh(topic_creat)

    return db_topic


@router.delete('/{topic_id}')
async def topic_delete(topic_id: int, session: db_dep, current_user: User = Depends(current_user_dep)):

    db_delete = session.query(Topic).first(Topic.id == topic_id).first()

    if not db_delete:
        raise HTTPException(status_code=404, detail="Bunday Topic topilmadi.")

    user_participations = session.query(Participation).filter(Participation.user_id == current_user.id).first()

    if user_participations:
        raise HTTPException(status_code=403, detail="O'yinchilar topic uchira olmaydi.")

    session.delete(db_delete)
    session.commit()

    return {"Topic muvaffaqiyatli o'chirildi"}
