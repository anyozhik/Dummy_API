import allure
import requests
from utilities.logger import Logger

"""Список HTTP методов"""

class HttpMethods:
    headers = {'Content-Type': 'application/json', 'app-id': '65d8573f7f66be2d8275a854'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("Method GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers = HttpMethods.headers, cookies = HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("Method POST"):
            Logger.add_request(url, method="POST")
            result = requests.post(url, json = body,  headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("Method PUT"):
            Logger.add_request(url, method="PUT")
            result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url):
        with allure.step("Method DELETE"):
            Logger.add_request(url, method="DELETE")
            result = requests.delete(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
            Logger.add_response(result)
            return result

class HttpMethodsWithoutAuthorization:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("Method GET"):
            Logger.add_request(url, method="GET")
            result = requests.get(url, headers=HttpMethodsWithoutAuthorization.headers, cookies=HttpMethodsWithoutAuthorization.cookie)
            Logger.add_response(result)
            return result
