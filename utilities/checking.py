"""Methods for checking responses"""
import json
import jsonschema
from jsonschema import validate

class Checking:

    """Method for checking a status code of response"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, "Error, Status code do not match."
        print(f"Successfully! Status code is {result.status_code}")

    """Method for checking required fields in response"""
    @staticmethod
    def check_json_token(result, expected_value):
        fields = json.loads(result.text)
        assert list(fields) == expected_value, "Error. The list of fields doesn't match with the expected one."
        print(list(fields))
        print("All fields are presented")

    """Method for checking values of required fields in response"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"Error. The value in the {field_name} isn't correct"
        print(check_info)
        print(f"{field_name} is correct!")

    """Method for checking nested values of required fields in response"""

    @staticmethod
    def check_json_value_nested(result, field_name, nested_field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name).get(nested_field_name)
        assert check_info == expected_value, f"Error. The value in the {nested_field_name} in {field_name} isn't correct"
        print(check_info)
        print(f"{nested_field_name} in {field_name} is correct!")


    """Method for checking nested values of required fields in lists in response"""

    @staticmethod
    def check_json_value_nested_lists(result, field_name, num_of_element_in_list, nested_field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)[num_of_element_in_list].get(nested_field_name)
        assert check_info == expected_value, f"Error. The value in the {nested_field_name} in {field_name} isn't correct"
        print(check_info)
        print(f"{nested_field_name} in {field_name} is correct!")

    """Method for checking values of required fields in response using search_word"""

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in  check_info, f"Error. The {search_word} in the {field_name} isn't presented"
        print(check_info)
        print(f"Word {search_word} in {field_name} is presented!")

    @staticmethod
    def check_json_schema(result, schema):
        result = json.loads(result.text)
        try:
            validate(instance=result, schema=schema)
            print("JSON schema is correct")
        except jsonschema.ValidationError as ex:
            print(ex)





