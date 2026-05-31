from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
import uuid

'''{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}'''

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def username(self)->str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self)->str:
        return f"{self.first_name} {self.last_name}"

class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "playwright"
    max_score: int = Field(alias="maxScore", default= 1000)
    min_score: int = Field(alias="minScore", default= 100)
    description: str = "Playwright course"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default= "2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")

course_default_model = CourseSchema(
    id="course_id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    previewFile=FileSchema(
        id="file_id",
        url="https://localhost:8000",
        filename="file_id",
        directory="courses"
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
    id="user_id",
    email= "user@mail.com",
    lastName= "Bond",
    firstName="Zara",
    middleName="Alice"
    )
)
print("course_default_model", course_default_model)

course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile":{
        "id":"file_id",
        "url":"https://localhost:8000",
        "filename":"file_id",
        "directory":"courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
    "id":"user_id",
    "email":"user@mail.com",
    "lastName":"Bond",
    "firstName":"Zara",
    "middleName":"Alice"
    }
}

course_dict_model = CourseSchema(**course_dict)
print("course_dict_model:", course_dict_model)


course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile":{
        "id":"file_id",
        "url":"https://localhost:8000",
        "filename":"file_id",
        "directory":"courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
    "id":"user_id",
    "email":"user@mail.com",
    "lastName":"Bond",
    "firstName":"Zara",
    "middleName":"Alice"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print("course_json_model:", course_json_model, type(course_json_model))
print(course_json_model.model_dump(by_alias=True), type(course_json_model.model_dump(by_alias=True)))
print(course_json_model.model_dump_json(by_alias=True), type(course_json_model.model_dump_json(by_alias=True)))

user = UserSchema(
    id="user_id",
    email="asdf@mail.com",
    lastName="Bond",
    firstName="Zara",
    middleName="Alice"
)
print(user.get_username(), user.username)

try:
    file = FileSchema(
        id="name",
        filename="name1",
        directory="courses",
        url='ht://localhost:8000'
    )
except ValidationError as e:
    print(e)
    print(e.errors())