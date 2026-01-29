import getters

def negative_assert_characters_is_less_than_the_lower_limit(name):

    user_response = getters.get_response_new_user()

    assert user_response.status_code == 201 # Created

    assert user_response.json()["authToken"] != "" # False

    kit_response = getters.get_response_new_kit(name)

    assert kit_response.status_code == 400, f"Se esperaba code: 400"

    # assert kit_response.json()["code"] == 400

    # assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

def negative_assert_characters_is_greater_than_the_upper_limit(name):

    user_response = getters.get_response_new_user()

    assert user_response.status_code == 201 # Created

    assert user_response.json()["authToken"] != "" # False

    kit_response = getters.get_response_new_kit(name)

    assert kit_response.status_code == 400, f"Se esperaba code: 400"

    # assert kit_response.json()["code"] == 400

    # assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

def negative_assert_no_key_name():

    user_response = getters.get_response_new_user()

    assert user_response.status_code == 201 # Created

    assert user_response.json()["authToken"] != "" # False

    kit_response = getters.get_response_new_kit_no_keys()

    assert kit_response.status_code == 400, f"Se esperaba code: 400"

    # assert kit_response.json()["code"] == 400

    # assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

def negative_assert_different_type(name):

    user_response = getters.get_response_new_user()

    assert user_response.status_code == 201 # Created

    assert user_response.json()["authToken"] != "" # False

    kit_response = getters.get_response_new_kit(name)

    assert kit_response.status_code == 400, f"Se esperaba code: 400"

    # assert kit_response.json()["code"] == 400

    # assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"