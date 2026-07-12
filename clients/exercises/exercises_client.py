from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, GetExercisesQuerySchema, \
    UpdateExerciseRequestSchema, ExerciseSchema, UpdateExerciseResponseSchema, GetExerciseResponseSchema, \
    GetExercisesResponseSchema, CreateExerciseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


# class GetExercisesQueryDict(TypedDict):
#     """
#     Описание структуры запроса на получение списка заданий.
#     """
#     courseId: str
#
#
# class CreateExerciseRequestDict(TypedDict):
#     """
#     Описание структуры запроса на создание задания.
#     """
#     title: str
#     courseId: str
#     maxScore: int
#     minScore: int
#     orderIndex: int
#     description: str
#     estimatedTime: str
#
# class UpdateExerciseRequestDict(TypedDict):
#     """
#     Описание структуры запроса на обновление задания.
#     """
#     title: str | None
#     maxScore: int | None
#     minScore: int | None
#     orderIndex: int | None
#     description: str | None
#     estimatedTime: str | None
#
#
# class Exercise(TypedDict):
#     """
#     Описание структуры задания.
#     """
#     id: str
#     title: str
#     courseId: str
#     maxScore: int
#     minScore: int
#     orderIndex: int
#     description: str
#     estimatedTime: str
#
# class UpdateExerciseResponseDict(TypedDict):
#     exercise: Exercise
#
# class GetExerciseResponseDict(TypedDict):
#     """
#     Описание структуры ответа на получение задания..
#     """
#     exercise: Exercise
#
# class GetExercisesResponseDict(TypedDict):
#     """
#     Описание структуры ответа на получение списка заданий.
#     """
#     exercises: list[Exercise]

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self,query: GetExercisesQuerySchema)-> Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/exercises', params=query)

    def get_exercise_api(self, exercise_id: str)-> Response:
        return self.get(f'/api/v1/exercises{exercise_id}')

    def create_exercise_api(self, request: CreateExerciseRequestSchema)-> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/exercises', json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema)-> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request.model_dump(exclude_none=True, by_alias=True))

    def delete_exercise_api(self, exercise_id: str)-> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')

    def get_exercises(self,query: GetExercisesQuerySchema)-> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str)->GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self,request: CreateExerciseRequestSchema)->CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self,exercise_id: str, request: UpdateExerciseRequestSchema)->GetExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return GetExerciseResponseSchema.model_validate_json(response.text)

def get_exercises_client(user: AuthenticationUserSchema)-> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(get_private_http_client(user))
