from sqlalchemy import false
from sqlalchemy.exc import IntegrityError
from app.models import User
from app.schemas import UserModel
from app.database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import HTTPException


crypt_context = CryptContext(schemes=['sha256_crypt'])


class UserCase:
    def __init__(self, user: UserModel, db_session: Session):
        self.__username = user.username
        self.__password = user.password
        self.__db_session = db_session

    def created_user(self):
        __user_model = User(
            username=self.__username,
            password=crypt_context.hash(self.__password)
        )
        try:
            self.__db_session.add(__user_model)
            self.__db_session.commit()
            self.__db_session.refresh(__user_model)
            return self.__username
        except IntegrityError:

            raise HTTPException(
                status_code=401, detail='Invalid username or password')

    def check_by_username(self):
        user = self.__db_session.query(User).where(
            User.username == self.__username).first()
        if user:
            raise HTTPException(
                status_code=400, detail='username ja exister')
        return false
