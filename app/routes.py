from app.schemas import UserModel
from app.depends import get_db, token_verifier
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.auth import UserCase
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix='/user')


@router.post('/register', status_code=201)
def user_register(user: UserModel, db_session: Session = Depends(get_db)):
    n_user = UserCase(user, db_session)
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
    result = n_user.login_user()
    return result


@router.get('/test')
def test_user_verify(dependencies=Depends(token_verifier)):
    return 'ok welocome api fastapi'
