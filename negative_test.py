import sender_stand_request
import getters

def negative_assert_characters_is_less_than_the_lower_limit(name):

    user_body = getters.get_user_body()

    headers_body = getters.get_headers()

    user_response = sender_stand_request.post_new_user(user_body, headers_body)

    assert user_response.status_code == 201 # Created

    assert user_response.json()["authToken"] != "" # False

    kit_body = getters.get_kit_body(name) # obtiene: {"name": name}

    headers_authToken_body = getters.get_headers_authToken(user_response.json()["authToken"])

    kit_response = sender_stand_request.post_new_kit(kit_body, headers_authToken_body)

    assert kit_response.status_code == 400, f"Se esperaba code: 400"

    # assert kit_response.json()["code"] == 400

    # assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

def negative_assert_characters_is_greater_than_the_upper_limit(name):

    user_body = getters.get_user_body()

    headers_body = getters.get_headers()

    user_response = sender_stand_request.post_new_user(user_body, headers_body)

    assert user_response.status_code == 201 # Created

    assert user_response.json()["authToken"] != "" # False

    kit_body = getters.get_kit_body(name) # obtiene: {"name": name}

    headers_authToken_body = getters.get_headers_authToken(user_response.json()["authToken"])

    kit_response = sender_stand_request.post_new_kit(kit_body, headers_authToken_body)

    assert kit_response.status_code == 400, f"Se esperaba code: 400"

    # assert kit_response.json()["code"] == 400

    # assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

def negative_assert_no_key_name():

    user_body = getters.get_user_body()

    headers_body = getters.get_headers()

    user_response = sender_stand_request.post_new_user(user_body, headers_body)

    assert user_response.status_code == 201 # Created

    assert user_response.json()["authToken"] != "" # False

    kit_body = getters.get_kit_no_body() # obtiene una lista vacía { }

    headers_authToken_body = getters.get_headers_authToken(user_response.json()["authToken"])

    kit_response = sender_stand_request.post_new_kit(kit_body, headers_authToken_body)

    assert kit_response.status_code == 400, f"Se esperaba code: 400"

    # assert kit_response.json()["code"] == 400

    # assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

def negative_assert_different_type(name):

    user_body = getters.get_user_body()

    headers_body = getters.get_headers()

    user_response = sender_stand_request.post_new_user(user_body, headers_body)

    assert user_response.status_code == 201 # Created

    assert user_response.json()["authToken"] != "" # False

    kit_body = getters.get_kit_body(name) # obtiene  { "name" : name }

    headers_authToken_body = getters.get_headers_authToken(user_response.json()["authToken"])

    kit_response = sender_stand_request.post_new_kit(kit_body, headers_authToken_body)

    assert kit_response.status_code == 400, f"Se esperaba code: 400"

    # assert kit_response.json()["code"] == 400

    # assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"