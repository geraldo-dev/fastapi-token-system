from app.schemas import UserModel
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.auth import UserCase, Toke
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

router = APIRouter(prefix='/user')

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')


# depends
def token_verifier(
    db_session: Session = Depends(get_db),
    token=Depends(oauth_scheme)
):
    uc = Toke(db_session)
    uc.token_verifier(access_token=token)


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
    result = n_user.login_user()
    return result


test_router = APIRouter(dependencies=[Depends(token_verifier)])


@test_router.get('/test')
def test_user_verify():
    return 'ok welocome api fastapi'
