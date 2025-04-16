from fastapi import APIRouter, HTTPException
from datetime import timezone, timedelta

from app.dependices import current_user_dep, db_dep
from app.schemas.game import *
from app.models.game import Game, GameQuestion
from app.models.topic import Topic
from app.models.participation import Participation
from app.models.user import User



router = APIRouter(
    prefix= '/Game',
    tags= ['game']
 )

@router.get("/", response_model=list[GameResponse])
async def get_games(db: db_dep):
    return db.query(Game).filter(
        Game.end_time > datetime.now(timezone.utc)
    )

@router.get('/', response_model=list[GameResponse])
async def get_game(session: db_dep):
    return session.query(Game).all()


@router.get('/{game_id}', response_model=GameResponse)
async def root_game(game_id: int, session: db_dep):
    game = session.query(Game).filter(Game.id == game_id).first()

    if not game:
        raise HTTPException(status_code=404, detail="Bunday uyin topilmadi")

    return game


@router.post('/create', response_model= GameResponse)
async def create_game(game: GameCreate, session: db_dep, current_user: current_user_dep):

    if game.start_time < datetime.now(timezone.utc):
        raise HTTPException(
            status_code=400,
            detail="Start time must be in the future."
        )

    if game.end_time - game.start_time < timedelta(hours=1):
        raise HTTPException(
            status_code=400,
            detail="Game must last at least 1 hour."
        )

    db_game = Game(**game.model_dump(), owner_id=current_user.id)

    session.add(db_game)
    session.commit()
    session.refresh(db_game)

    return db_game


@router.patch('/update/{game_id}', response_model= GameResponse)
async def update_game(game_id: int, game: GameUpdate, session: db_dep, current_user: current_user_dep):

    db_game = session.query(Game).filter(Game.id == game_id).first()

    if not db_game:
        raise HTTPException(status_code=404, detail="Bunday id dagi o'yin topilmadi.")

    db_game.title = game.title if game.title else db_game.title
    db_game.description = game.description if game.description else db_game.description
    db_game.end_time = game.end_time if game.end_time else db_game.end_time
    db_game.topic_id = game.topic_id if game.topic_id else db_game.topic_id

    session.commit()
    session.refresh(db_game)

    return db_game

@router.delete('/{game_id')
async def delete_game(game_id: int, session: db_dep, current_user: current_user_dep):

    db_delete = session.query(Game).filter(Game.id == game_id).first()

    if not db_delete:
        raise HTTPException(status_code=403, detail="Game not found")

    session.delete(db_delete)
    session.commit()

    return {
        "game_id": id,
        "message": "Game deleted."
    }




