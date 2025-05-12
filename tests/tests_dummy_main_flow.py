import allure

from utilities.api import DummyApi
from utilities.checking import Checking

"""Creating, updating, deleting a new user, a post and a comment for this post"""
@allure.epic("Test for creating a new user, a post and a comment for this post")
class TestCreateUserPostComment:

    @allure.description("Test for creating a new user, a post and a comment for this post")
    def test_create_new_user_post_comment(self):

        print("Method post for a user")
        post_result = DummyApi.create_new_user()
        check_post = post_result.json()
        user_id = check_post.get("id")
        Checking.check_status_code(post_result, 200)
        Checking.check_json_token(post_result, ['id', 'firstName', 'lastName', 'gender', 'email', 'registerDate', 'updatedDate'])
        print(f"\n")

        print("Method get after post for the user")
        get_result = DummyApi.get_new_user(user_id)
        Checking.check_status_code(get_result, 200)
        print(f"\n")

        print("Method put for the user")
        put_result = DummyApi.put_new_user(user_id)
        Checking.check_status_code(put_result, 200)
        Checking.check_json_value(put_result, 'firstName', 'Alla')
        Checking.check_json_value(put_result, 'phone', '+7-980-555-6699')
        Checking.check_json_value_nested(put_result, 'location', 'city', 'Moscow')
        Checking.check_json_token(put_result,
                                  ['id', 'firstName', 'lastName', 'gender', 'email', 'phone', 'location', 'registerDate', 'updatedDate'])
        print(f"\n")

        print("Method post for a new post")
        post_result = DummyApi.create_new_post(user_id)
        check_post = post_result.json()
        post_id = check_post.get("id")
        Checking.check_status_code(post_result, 200)
        Checking.check_json_token(post_result,
                                  ['id', 'image', 'likes', 'link', 'tags', 'text', 'publishDate', 'updatedDate', 'owner'])
        Checking.check_json_value(post_result, 'text', 'Life is cool!')
        Checking.check_json_value_nested(post_result, 'owner', 'id', user_id)
        print(f"\n")

        print("Method get after post for the new post")
        get_result = DummyApi.get_new_post(post_id)
        Checking.check_status_code(get_result, 200)
        print(f"\n")

        print("Method put for the new post")
        put_result = DummyApi.put_new_post(post_id)
        Checking.check_status_code(put_result, 200)
        Checking.check_json_value(put_result, 'likes', 1313)
        print(f"\n")

        print("Method post for a new comment")
        post_result = DummyApi.create_new_comment(user_id, post_id)
        check_post = post_result.json()
        comment_id = check_post.get("id")
        Checking.check_status_code(post_result, 200)
        Checking.check_json_token(post_result,
                                  ['id', 'message', 'owner', 'post', 'publishDate'])
        Checking.check_json_value(post_result, 'message', 'how cool is that')
        Checking.check_json_value_nested(post_result, 'owner', 'id', user_id)
        Checking.check_json_value(post_result, 'post', post_id)
        print(f"\n")

        print("Method get for a comment using User id")
        get_result = DummyApi.get_comments_by_user(user_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_value_nested_lists(get_result, 'data', 0, 'id', comment_id)
        Checking.check_json_value(get_result, 'total', 1)
        print(f"\n")

        print("Method delete for the comment")
        delete_result = DummyApi.delete_new_comment(comment_id)
        Checking.check_status_code(delete_result, 200)
        Checking.check_json_token(delete_result, ['id'])
        Checking.check_json_value(delete_result, 'id', comment_id)
        print(f"\n")

        print("Method get for a comment using User id")
        get_result = DummyApi.get_comments_by_user(user_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_value(get_result, 'total', 0)
        print(f"\n")

        print("Method delete for the post")
        delete_result = DummyApi.delete_new_post(post_id)
        Checking.check_status_code(delete_result, 200)
        Checking.check_json_token(delete_result, ['id'])
        Checking.check_json_value(delete_result, 'id', post_id)
        print(f"\n")

        print("Method get after delete for the post")
        get_result = DummyApi.get_new_post(post_id)
        Checking.check_status_code(get_result, 404)
        Checking.check_json_value(get_result, 'error', 'RESOURCE_NOT_FOUND')
        print(f"\n")

        print("Method delete for the user")
        delete_result = DummyApi.delete_new_user(user_id)
        Checking.check_status_code(delete_result, 200)
        Checking.check_json_token(delete_result, ['id'])
        Checking.check_json_value(delete_result, 'id', user_id)
        print(f"\n")

        print("Method get after delete for the user")
        get_result = DummyApi.get_new_post(user_id)
        Checking.check_status_code(get_result, 404)
        Checking.check_json_value(get_result, 'error', 'RESOURCE_NOT_FOUND')
        print(f"\n")

        print("Testing of creating, updating and deleting a new user, a post and a comment has finished successfully.")
