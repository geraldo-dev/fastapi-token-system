from sqlalchemy.orm import Session
from fastapi import Depends
from app.auth import Toke
from fastapi.security import OAuth2PasswordBearer
from app.database import SessionLocal

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def token_verifier(
    db_session: Session = Depends(get_db),
    token=Depends(oauth_scheme)
):
    uc = Toke(db_session)
    uc.token_verifier(access_token=token)
