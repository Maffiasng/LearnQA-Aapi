from requests import request
import json

class Assertion:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_massage):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not on JSON format. Response text is '{response.text}'"

        assert name is response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value,error_massage
