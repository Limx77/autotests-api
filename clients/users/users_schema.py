from pydantic import BaseModel, Field, ConfigDict


class UserSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)
    """
    Настройка, позволяющая создавать модели прописываю в аргументах
    как alias так и python именование(CamelCase или snake_case)
    """

    id: str
    email: str
    last_name: str = Field(alias= 'lastName')
    first_name: str = Field(alias= 'firstName')
    middle_name: str = Field(alias= 'middleName')

class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)
    """
    Настройка, позволяющая создавать модели прописываю в аргументах
    как alias так и python именование(CamelCase или snake_case)
    """
    email: str | None
    last_name: str | None = Field(alias= 'lastName')
    first_name: str | None = Field(alias= 'firstName')
    middle_name: str | None = Field(alias= 'middleName')

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config= ConfigDict(populate_by_name=True)
    """
    Настройка, позволяющая создавать модели прописываю в аргументах
    как alias так и python именование(CamelCase или snake_case)
    """

    email: str
    password: str
    last_name: str = Field(alias= 'lastName')
    first_name: str = Field(alias= 'firstName')
    middle_name: str = Field(alias= 'middleName')

class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления пользователя.
    """

    user: UserSchema

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema