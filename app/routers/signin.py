from typing import Annotated

import jwt
from sqlalchemy import select
from fastapi import APIRouter, status as HTTPException, Depends
from sqlalchemy.orm import Session

from app.dependices import get_db
from app.schemas.login import LoginSchema, SignupSchema
from app.schemas.users import UserSchema
from app.models import User
from app.utils.auth import hash_password, dehash_password

router = APIRouter(
    prefix="/authentication",
    tags=["Authentication"],
)


@router.post(
    "/signup",
    name="Signup Endpoint",
)
def signup(
        signup_data: SignupSchema,
        db_session: Annotated[Session, Depends(get_db)]
):
    data = signup_data.model_dump()
    data['hashed_password'] = hash_password(data['password'])

    data.pop('password')

    try:
        entry = User(**data)
        db_session.add(entry)
        db_session.commit()
    except Exception as e:
        raise e

    data.pop('hashed_password')

    access_token = jwt.encode(data, "secret", algorithm="HS256")

    return {"detail": data, "token": access_token}


@router.post(
    path="/signin",
    response_model=""
)
def signin(
        login_payload: LoginSchema,
        db_session: Annotated[Session, Depends(get_db)],
):
    username = login_payload.username

    user_stmt = select(User).where(User.username == username)
    user_query = db_session.execute(user_stmt).first()

    if user_query is None:
        return HTTPException(status_code=404, detail="User not found")

    user = user_query[0]

    user_dict = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        # "birthdate": user.birthdate
    }

    user_data = UserSchema.model_validate(user_dict)

    user_data_payload = user_data.model_dump()

    access_token = jwt.encode(user_data_payload, "secret", algorithm="HS256")

    return {"jwt": access_token}


# @router(
#     "/simple"
# )
# def simple_endpoint(
#         db_session: Annotated[Session, Depends(get_db)],
#         auth_token: Annotated[UserSchema, Depends(get_token_data)]
# ):
#     pass