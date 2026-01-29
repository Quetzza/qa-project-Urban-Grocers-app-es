import sender_stand_request
import data

def get_kit_body(name):

    current_body = data.kit_body.copy()

    current_body["name"] = name

    return current_body

def get_kit_no_body():

    curren_body = data.kit_body.copy()

    curren_body.pop("name")

    return curren_body

def get_headers():

    current_headers = data.headers.copy()

    return current_headers

def get_headers_authToken():

    current_headers = data.headers.copy()

    current_headers["Authorization"] = 'Bearer ' + get_new_user_token()

    return current_headers

def get_user_body():

    current_user_body = data.user_body.copy()

    return current_user_body

def get_new_user_token():

    current_authToken = data.user_authToken.copy()

    response = get_response_new_user()

    current_authToken["authToken"] =  response.json()["authToken"]

    return current_authToken["authToken"] 

def get_response_new_user():
    
    return sender_stand_request.post_new_user(get_user_body(), get_headers())

def get_response_new_kit(name):

    return sender_stand_request.post_new_kit(get_kit_body(name), get_headers_authToken())

def get_response_new_kit_no_keys():

    return sender_stand_request.post_new_kit(get_kit_no_body(), get_headers_authToken())
