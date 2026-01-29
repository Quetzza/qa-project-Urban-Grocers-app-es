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

def get_headers_authToken(token):

    current_headers = data.headers.copy()

    current_headers["Authorization"] = 'Bearer ' + token

    return current_headers

def get_user_body():

    current_user_body = data.user_body.copy()

    return current_user_body

