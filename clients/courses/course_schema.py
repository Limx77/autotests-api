from pydantic import BaseModel, Field, ConfigDict, model_validator
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from fixtures.users import UserFixture
from tools.fakers import fake

class CourseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)
    """
    Описание структуры курса.
    """
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema

class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    title: str = Field(default_factory=fake.text)
    max_score: int = Field(alias="maxScore", default=None)
    min_score: int = Field(alias="minScore", default=None)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias='previewFileId')
    created_by_user_id: str = Field(alias='createdByUserId')

    @model_validator(mode="after")
    def fill_scores(self):
        """
        Функция, которая после создания модели заполняет ее поля min и max score
        :return: экземпляр модели CreateCourseRequestSchema
        """
        if self.min_score is None:
            self.min_score = fake.integer(0, 50)

        if self.max_score is None:
            self.max_score = fake.integer(self.min_score, 100)

        return self


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None = Field(default_factory=fake.text)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.integer)
    min_score: int | None = Field(alias="minScore", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class UpdateCourseResponseSchema(BaseModel):
    course: CourseSchema

class GetCoursesResponseSchema(BaseModel):
    courses: list[CourseSchema]

class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

    user_id: str = Field(alias='userId')
