# from app.models import User
from app.schemas import UserModel, UserModelResponse
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.auth import UserCase
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix='/user')  # accounts sign


@router.post('/register', status_code=201)
def user_register(user: UserModel, db_session: Session = Depends(get_db)):
    n_user = UserCase(user, db_session)
    # valida se ja exite esse usuario
    n_user.check_by_username()

    return n_user.created_user()


@router.post('/login', status_code=200)
def user_login(
        user: OAuth2PasswordRequestForm = Depends(),
        db_session: Session = Depends(get_db)):

    # schema
    s_user = UserModel(
        username=user.username,
        password=user.password)

    # model
    n_user = UserCase(s_user, db_session)

    return n_user.login_user()
