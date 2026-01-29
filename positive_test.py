import sender_stand_request
import getters

def positive_assert(name):

    user_response = getters.get_response_new_user() # Get data user

    assert user_response.status_code == 201 # Created

    assert user_response.json()["authToken"] != "" # False

    kit_response = getters.get_response_new_kit(name) # Get data kit

    assert kit_response.status_code == 201 # Created

    assert kit_response.json()["name"] == name # True

