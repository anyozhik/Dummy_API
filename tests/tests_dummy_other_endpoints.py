import allure
from utilities.api import DummyApi
from utilities.checking import Checking
from utilities.schemas import SchemasDummy

"""Checking other endpoints that are not included in the main flow"""
@allure.epic("Test for checking other endpoints that are not included in the main flow")
class TestCheckOtherEndpoints:

    @allure.description("Test for checking endpoint with the full user list")
    def test_full_user_list(self):
        print("Method get for the list of all users")
        get_result = DummyApi.get_user_list()
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, ['data', 'total', 'page', 'limit'])
        schema = SchemasDummy.user_list_schema
        Checking.check_json_schema(get_result, schema)

    def test_full_user_list_with_params(self):
        print("Method get for the list of all users with parameters")
        page = 1
        limit = 50
        get_result = DummyApi.get_user_list_with_params(page, limit)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, ['data', 'total', 'page', 'limit'])
        schema = SchemasDummy.user_list_schema
        Checking.check_json_schema(get_result, schema)
        Checking.check_json_value(get_result, 'page', page)
        Checking.check_json_value(get_result, 'limit', limit)

    def test_full_user_list_with_params_invalid(self):
        print("Method get for the list of all users with parameters")
        get_result = DummyApi.get_user_list_with_params("A", "A")
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, ['data', 'total', 'page', 'limit'])
        schema = SchemasDummy.user_list_schema
        Checking.check_json_schema(get_result, schema)
        Checking.check_json_value(get_result, 'page', None)
        Checking.check_json_value(get_result, 'limit', None)

    def test_full_user_without_authorization(self):  #523
        print("Method get for the list of all users without authorization")
        get_result = DummyApi.get_user_list_without_authorization()
        Checking.check_status_code(get_result, 403)
        Checking.check_json_value(get_result, 'error', 'APP_ID_MISSING')


    @allure.description("Test for checking endpoint with the full post list")
    def test_full_post_list(self):
        print("Method get for the list of all posts")
        get_result = DummyApi.get_post_list()
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, ['data', 'total', 'page', 'limit'])
        schema = SchemasDummy.post_list_schema
        Checking.check_json_schema(get_result, schema)

    def test_full_post_list_with_params(self):
        print("Method get for the list of all posts with parameters")
        page = 3
        limit = 20
        get_result = DummyApi.get_post_list_with_params(page, limit)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, ['data', 'total', 'page', 'limit'])
        schema = SchemasDummy.post_list_schema
        Checking.check_json_schema(get_result, schema)
        Checking.check_json_value(get_result, 'page', page)
        Checking.check_json_value(get_result, 'limit', limit)

    def test_full_post_list_with_params_invalid(self):
        print("Method get for the list of all posts with invalid parameters")
        get_result = DummyApi.get_user_list_with_params("A", "A")
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, ['data', 'total', 'page', 'limit'])
        schema = SchemasDummy.post_list_schema
        Checking.check_json_schema(get_result, schema)
        Checking.check_json_value(get_result, 'page', None)
        Checking.check_json_value(get_result, 'limit', None)

    @allure.description("Test for checking endpoint with the full tag list")
    def test_full_tag_list(self):
        print("Method get for the list of all tags")
        get_result = DummyApi.get_tag_list()
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, ['data'])
        print(f"Number of tags {len(get_result.text)}")



















