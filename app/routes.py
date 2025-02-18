# from app.models import User
from app.schemas import UserModel, UserModelResponse
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.auth import UserCase

router = APIRouter(prefix='/user')  # accounts sign


@router.post('/register', status_code=201)
def user_register(user: UserModel, db_session: Session = Depends(get_db)):
    n_user = UserCase(user, db_session)
    # valida se ja exite esse usuario
    n_user.check_by_username()

    return n_user.created_user()
