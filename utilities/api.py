from utilities.http_methods import HttpMethods
from utilities.http_methods import HttpMethodsWithoutAuthorization
from faker import Faker

faker = Faker("en_US")

"""Methods for testing Dummy API"""

base_url = "https://dummyapi.io/data/v1" #base URL

class DummyApi:
    """Method for creating a new user"""
    @staticmethod
    def create_new_user():

        json_for_create_new_user = {
        "firstName": f"{faker.first_name_female()}",
        "lastName": f"{faker.last_name_female()}",
        "gender": "female",
        "email": f"{faker.email()}"
        }

        post_resource = "/user/create"

        post_url = f"{base_url}{post_resource}"
        print(post_url)

        result_post = HttpMethods.post(post_url, json_for_create_new_user)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    """Method for checking a new user"""
    @staticmethod
    def get_new_user(user_id):

        get_resource = "/user/" #resource for a get request
        get_url = f"{base_url}{get_resource}{user_id}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Method for updating a new user"""

    @staticmethod
    def put_new_user(user_id):
        put_resource = "/user/"  # resource for a put request
        put_url = f"{base_url}{put_resource}{user_id}"
        print(put_url)

        json_for_update_new_user = {
        "firstName": "Alla",
        "phone": "+7-980-555-6699",
            "location": {
                "street": "Lenina",
                "city": "Moscow",
                "country": "Russian Federation",
                "timezone": "+7.00"
            }
        }

        result_put = HttpMethods.put(put_url, json_for_update_new_user)
        print(result_put.json())
        print(result_put.status_code)
        return result_put

    """Method for deleting a new user"""

    @staticmethod
    def delete_new_user(user_id):
        delete_resource = "/user/"  # resource for a delete request
        delete_url = f"{base_url}{delete_resource}{user_id}"
        print(delete_url)

        result_delete = HttpMethods.delete(delete_url)
        print(result_delete.json())
        print(result_delete.status_code)
        return result_delete

    """Method for creating a new post"""
    @staticmethod
    def create_new_post(user_id):

        json_for_create_new_post = {
        "text": "Life is cool!",
        "likes": 13,
        "tags": ["lifecoding", "loveiseverywhere"],
        "owner": f"{user_id}"
        }

        post_resource = "/post/create"

        post_url = f"{base_url}{post_resource}"
        print(post_url)

        result_post = HttpMethods.post(post_url, json_for_create_new_post)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    """Method for checking a new post"""
    @staticmethod
    def get_new_post(post_id):

        get_resource = "/post/" #resource for a get request
        get_url = f"{base_url}{get_resource}{post_id}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Method for updating a new post"""

    @staticmethod
    def put_new_post(post_id):
        put_resource = "/post/"  # resource for a put request
        put_url = f"{base_url}{put_resource}{post_id}"
        print(put_url)

        json_for_update_new_post = {
        "likes": 1313
        }

        result_put = HttpMethods.put(put_url, json_for_update_new_post)
        print(result_put.json())
        print(result_put.status_code)
        return result_put

    """Method for deleting a new post"""

    @staticmethod
    def delete_new_post(post_id):
        delete_resource = "/post/"  # resource for a delete request
        delete_url = f"{base_url}{delete_resource}{post_id}"
        print(delete_url)

        result_delete = HttpMethods.delete(delete_url)
        print(result_delete.json())
        print(result_delete.status_code)
        return result_delete


    """Method for creating a new comment"""
    @staticmethod
    def create_new_comment(user_id, post_id):

        json_for_create_new_comment = {
        "message": "how cool is that",
        "owner": f"{user_id}",
        "post": f"{post_id}"
        }

        post_resource = "/comment/create"

        post_url = f"{base_url}{post_resource}"
        print(post_url)

        result_post = HttpMethods.post(post_url, json_for_create_new_comment)
        print(result_post.json())
        print(result_post.status_code)
        return result_post

    """Method for checking a new comment by User"""
    @staticmethod
    def get_comments_by_user(user_id):

        get_resource = f"/user/{user_id}/comment" #resource for a get request
        get_url = f"{base_url}{get_resource}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Method for deleting a new comment"""

    @staticmethod
    def delete_new_comment(comment_id):
        delete_resource = "/comment/"  # resource for a delete request
        delete_url = f"{base_url}{delete_resource}{comment_id}"
        print(delete_url)
        result_delete = HttpMethods.delete(delete_url)
        print(result_delete.json())
        print(result_delete.status_code)
        return result_delete

    """Method for getting user list"""

    @staticmethod
    def get_user_list():
        get_resource = "/user"  # resource for a get request
        get_url = f"{base_url}{get_resource}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Method for getting user list"""

    @staticmethod
    def get_user_list_with_params(page, limit):
        get_resource = "/user"  # resource for a get request
        get_url = f"{base_url}{get_resource}?page={page}&limit={limit}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Method for getting user list without authorization"""

    @staticmethod
    def get_user_list_without_authorization():
        get_resource = "/user"  # resource for a get request
        get_url = f"{base_url}{get_resource}"
        print(get_url)

        result_get = HttpMethodsWithoutAuthorization.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    @staticmethod
    def get_post_list():
        get_resource = "/post"  # resource for a get request
        get_url = f"{base_url}{get_resource}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get

    """Method for getting user list"""

    @staticmethod
    def get_post_list_with_params(page, limit):
        get_resource = "/post"  # resource for a get request
        get_url = f"{base_url}{get_resource}?page={page}&limit={limit}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get


    @staticmethod
    def get_tag_list():
        get_resource = "/tag"  # resource for a get request
        get_url = f"{base_url}{get_resource}"
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)
        return result_get


