from pydantic import BaseModel, Field


class UserModel(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
