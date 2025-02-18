from pydantic import BaseModel, Field


class UserModel(BaseModel):
    username: str = Field(...)
    password: str = Field(...)


class UserModelResponse(BaseModel):
    id: str
    username: str
