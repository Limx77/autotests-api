import allure

from clients.courses.course_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tests.base import assert_equal
from tools.assertions.base import assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
from tools.logger import get_logger

logger = get_logger('COURSES_ASSERTIONS')


@allure.step("Check update course response")
def assert_update_course_response(request: UpdateCourseRequestSchema, response: UpdateCourseResponseSchema):
    logger.info("Check update course response")
    assert_equal(request.title, response.course.title, "title")
    assert_equal(request.max_score, response.course.max_score, "max_score")
    assert_equal(request.min_score, response.course.min_score, "min_score")
    assert_equal(request.description, response.course.description, "description")
    assert_equal(request.estimated_time, response.course.estimated_time, "estimated_time")

@allure.step("Check course")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    logger.info("Check course")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_user(actual.created_by_user, expected.created_by_user)
    assert_file(actual.preview_file, expected.preview_file)


@allure.step("Check get courses response")
def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]
):
    logger.info("Check get courses response")
    assert_length(get_courses_response.courses, create_course_responses, "courses")
    for index,create_course_response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_response.course)

@allure.step("Check create course response")
def assert_create_course_response(
        actual: CreateCourseRequestSchema,
        expected:CreateCourseResponseSchema
):
    """
    Проверяет, что создание курса соответсвует запросу
    :param actual: исходящий запрос, то есть актуальный
    :param expected: ответ API с данными курса
    :raises: AssertionError: Если хотябы одно значение не совпадает
    """
    logger.info("Check create course response")
    assert_equal(actual.title, expected.course.title, "title")
    assert_equal(actual.max_score, expected.course.max_score, "max_score")
    assert_equal(actual.min_score, expected.course.min_score, "min_score")
    assert_equal(actual.description, expected.course.description, "description")
    assert_equal(actual.estimated_time, expected.course.estimated_time, "estimated_time")
    assert_equal(actual.preview_file_id, expected.course.preview_file.id, "preview_file_id")
    assert_equal(actual.created_by_user_id, expected.course.created_by_user.id, "created_by_user_id")
