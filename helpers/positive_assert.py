from api import sender_stand_request
from data import data

def response_201(kit_body,auth_token):

    current_header = data.headers.copy()

    current_header["Authorization"] = "Bearer " + auth_token

    kit_response = sender_stand_request.post_new_client_kit(kit_body,current_header)

    assert kit_response.status_code == 201

    assert kit_response.json()["name"] == kit_body["name"]