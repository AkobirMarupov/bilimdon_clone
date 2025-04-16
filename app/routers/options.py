from fastapi import APIRouter, HTTPException

from app.dependices import db_dep, current_user_dep
from app.models import Option
from app.schemas.option import  OptionCreate, OptionUpdate, OptionResponse


router = APIRouter(
    prefix="/options",
    tags=["options"]
 )


@router.get("/", response_model=list[OptionResponse])
async def get_options(db: db_dep):
    return db.query(Option).all()


@router.get("/{option_id}", response_model=OptionResponse)
async def get_option(option_id: int, db: db_dep):
    option = db.query(Option).filter(Option.id == option_id).first()

    if not option:
        raise HTTPException(
            status_code=404,
            detail="Option not found."
        )

    return option


@router.post("/create/", response_model=OptionResponse)
async def create_option(
        option: OptionCreate,
        db: db_dep,
        current_user: current_user_dep
    ):
    existing_correct_option = db.query(Option).filter(
        Option.question_id == option.question_id,
        Option.is_correct == True
    ).first()

    if existing_correct_option and option.is_correct:
        raise HTTPException(
            status_code=400,
            detail="Question already has a correct option."
        )

    db_option = Option(
        **option.model_dump()
        )

    db.add(db_option)
    db.commit()
    db.refresh(db_option)

    return db_option


@router.put("/update/{option_id}", response_model=OptionResponse)
async def update_option(
        option_id: int,
        option: OptionUpdate,
        db: db_dep
    ):
    db_option = db.query(Option).filter(Option.id == option_id).first()

    if not db_option:
        raise HTTPException(
            status_code=404,
            detail="Option not found."
        )

    db_option.title = option.title if option.title else db_option.title
    db_option.is_correct = option.is_correct if option.is_correct else db_option.is_correct

    db.commit()
    db.refresh(db_option)

    return db_option


@router.delete("/delete/{option_id}")
async def delete_option(option_id: int, db: db_dep):
    db_option = db.query(Option).filter(Option.id == option_id).first()

    if not db_option:
        raise HTTPException(
            status_code=404,
            detail="Option not found."
        )

    db.delete(db_option)
    db.commit()

    return {
        "option_id": id,
        "message": "Option deleted."
    }