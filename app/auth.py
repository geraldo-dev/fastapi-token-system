from sqlalchemy.exc import IntegrityError
from app.models import User
from app.schemas import UserModel
from app.database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import HTTPException


crypt_context = CryptContext(schemes=['sha256_crypt'])


class UserCase:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def created_user(self, user: UserModel):
        user_model = User(
            username=user.username,
            password=crypt_context.hash(user.password)
        )
        try:
            self.db_session.add(user_model)
            self.db_session.commit()
            self.db_session.refresh(user_model)
            return {'username': user_model.username}
        except IntegrityError:
            raise HTTPException(
                status_code=401, detail='Invalid username or password')
