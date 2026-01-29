import sender_stand_request
import getters

def positive_assert(name):

    user_body = getters.get_user_body()

    headers_body = getters.get_headers()

    user_response = sender_stand_request.post_new_user(user_body, headers_body)

    assert user_response.status_code == 201 # Created

    assert user_response.json()["authToken"] != "" # False

    kit_body = getters.get_kit_body(name)

    headers_authToken_body = getters.get_headers_authToken(user_response.json()["authToken"])

    kit_response = sender_stand_request.post_new_kit(kit_body, headers_authToken_body)

    assert kit_response.status_code == 201 # Created

    assert kit_response.json()["name"] == name # True

