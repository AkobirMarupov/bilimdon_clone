from fastapi import APIRouter, Depends, HTTPException

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


@router.get('/', response_model=list[GameResponse])
async def get_game(session: db_dep):
    db_game = session.query(Game).all()

    return db_game


@router.get('/{game_id}', response_model=GameResponse)
async def root_game(game_id: int, session: db_dep):
    game_gaet = session.query(Game).filter(Game.id == game_id).first()

    if not game_gaet:
        raise HTTPException(status_code=404, detail="Bunday uyin topilmadi")

    return game_gaet
