from http import HTTPStatus

import allure
import pytest
from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tests.base import assert_status_code
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from tools.allure.tags import AllureTag
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake


@pytest.mark.exercises
@pytest.mark.regression
@allure.tag(AllureTag.EXERCISES, AllureTag.REGRESSION)
@allure.feature(AllureFeatures.EXERCISES)
class TestExercises:

    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.title("Create Exercise")
    @allure.story(AllureStories.CREATE_ENTITY)
    @allure.step('Create exercise')
    def test_create_exercise(self,
            function_course: CourseFixture,
            exercises_client: ExercisesClient):
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("Get Exercise")
    @allure.story(AllureStories.GET_ENTITY)
    @allure.step('Get exercise')
    def test_get_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @pytest.mark.parametrize("update_request", [
        UpdateExerciseRequestSchema(title=fake.sentence()),
        UpdateExerciseRequestSchema(max_score=fake.max_score()),
        UpdateExerciseRequestSchema(min_score=fake.min_score()),
        UpdateExerciseRequestSchema(order_index=fake.integer()),
        UpdateExerciseRequestSchema(description=fake.text()),
        UpdateExerciseRequestSchema(estimated_time=fake.estimated_time()),
        UpdateExerciseRequestSchema(),
    ])
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("Update Exercise")
    @allure.story(AllureStories.UPDATE_ENTITY)
    @allure.step('Update exercise')
    def test_update_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture, update_request):
        print(update_request.model_dump(exclude_none=True, by_alias=True))
        response = exercises_client.update_exercise_api(function_exercise.response.exercise.id, update_request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        assert_update_exercise_response(update_request, response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @allure.tag(AllureTag.DELETE_ENTITY)
    @allure.title("Delete Exercise")
    @allure.story(AllureStories.DELETE_ENTITY)
    @allure.step('Delete exercise')
    def test_delete_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        exercise_id = exercises_client.create_exercise_api(function_exercise.request).json()["exercise"]["id"]
        print(exercise_id)
        response = exercises_client.delete_exercise_api(exercise_id)
        print(response.json())
        response_after_delete = exercises_client.get_exercise_api(exercise_id)
        response_after_delete_data = InternalErrorResponseSchema.model_validate_json(response_after_delete.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_status_code(response_after_delete.status_code, HTTPStatus.NOT_FOUND)

        assert_exercise_not_found_response(response_after_delete_data)

        validate_json_schema(instance=response_after_delete.json(), schema=response_after_delete_data.model_json_schema())


