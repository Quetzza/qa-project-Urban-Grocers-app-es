import positive_test
import negative_test
import sender_stand_request
import data
import get_kit_body
def positive_assert(name):
    
    user_body = data.user_body.copy()

    header = data.headers.copy() 
    
    # Create User
    user_response = sender_stand_request.post_new_user(user_body, header)

    # Code response 201 Created
    assert user_response.status_code == 201

    # Check user token
    assert user_response.json()["authToken"] != ""

    token = data.user_authToken.copy()

    # Save token
    token["authToken"] = user_response.json()["authToken"]

    kit_body = get_kit_body(name)

    header["Authorization"] = "Bearer " + kit_body["authToken"]

    # Create new kit 
    kit_response = sender_stand_request.post_new_kit(kit_body,header)

    # Code response 201 Created
    assert kit_response.status_code == 201

    # Check field name vs response field name
    assert kit_response.json()["name"] == name
"""
    TEST 1
    
    Descripción:
    El número permitido de caracteres (1): kit_body = { "name": "a"}

    Resultado esperado:
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
"""
def test_create_new_kit_name_1_character_get_success_response():
    positive_test.positive_assert("a")

"""
    TEST 2

    Descripción:
    El número permitido de caracteres (511): kit_body = {    "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

    Resultado esperado:
    Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
"""
def test_create_new_kit_name_511_character_get_success_response():
    positive_test.positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

"""
    TEST 3

    Descripción:
    El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }

    Resultado esperado:
    Código de respuesta: 400
"""
def test_create_new_kit_name_0_character_get_error_response():
    negative_test.negative_assert_characters_is_less_than_the_lower_limit("")

"""
    TEST 4

    Descripción:
    El número de caracteres es mayor que la cantidad permitida (512): kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}

    Resultado esperado:
    Código de respuesta: 400
"""
def test_create_new_kit_name_512_character_get_error_response():
    negative_test.negative_assert_characters_is_greater_than_the_upper_limit("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

"""
    TEST 5

    Descripción:
    Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }

    Resultado esperado:
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
"""
def test_create_new_kit_name_symbol_get_success_response():
    positive_test.positive_assert("\"№%@\",")

"""
    TEST 6

    Descripción:
    Se permiten espacios: kit_body = { "name": " A Aaa " }

    Resultado esperado:
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
"""
def test_create_new_kit_name_space_get_success_response():
    positive_test.positive_assert(" A Aaa ")

"""
    TEST 7

    Descripción:
    Se permiten números: kit_body = { "name": "123" }

    Resultado esperado:
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
"""
def test_create_new_kit_name_numbers_get_success_response():
    positive_test.positive_assert("123")

"""
    TEST 8

    Descripción:
    El parámetro no se pasa en la solicitud: kit_body = { }

    Resultado esperado:
    Código de respuesta: 400
"""
def test_create_new_kit_name_no_key_name_get_error_response():
    negative_test.negative_assert_no_key_name()

"""
    TEST 9

    Descripción:
    Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }

    Resultado esperado:
    Código de respuesta: 400
"""
def test_create_new_kit_name_different_types_get_error_response():
    negative_test.negative_assert_different_type(123)