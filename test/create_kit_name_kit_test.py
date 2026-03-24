from helpers.get_kit_body import get_kit_body
from helpers.get_auth_token import get_auth_token
from helpers.positive_assert import response_201
from helpers.negative_assert import response_400
from data import data
"""
    TEST 1
    
    Descripción:
    El número permitido de caracteres (1): kit_body = { "name": "a"}

    Resultado esperado:
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
"""
def test_create_new_kit_name_1_character_get_success_response():

    kit_body = get_kit_body("a")
    auth_token = get_auth_token()
    
    
    response_201(kit_body, auth_token)

"""
    TEST 2

    Descripción:
    El número permitido de caracteres (511): kit_body = {    "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

    Resultado esperado:
    Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
"""
def test_create_new_kit_name_511_character_get_success_response():

    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

    auth_token = get_auth_token()

    response_201(kit_body, auth_token)

"""
    TEST 3

    Descripción:
    El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }

    Resultado esperado:
    Código de respuesta: 400
"""
def test_create_new_kit_name_0_character_get_error_response():

    kit_body = get_kit_body("")
    auth_token = get_auth_token()

    response_400(kit_body, auth_token)

"""
    TEST 4

    Descripción:
    El número de caracteres es mayor que la cantidad permitida (512): kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}

    Resultado esperado:
    Código de respuesta: 400
"""
def test_create_new_kit_name_512_character_get_error_response():

    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

    auth_token = get_auth_token()

    response_400(kit_body, auth_token)

"""
    TEST 5

    Descripción:
    Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }

    Resultado esperado:
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
"""
def test_create_new_kit_name_symbol_get_success_response():
   
   kit_body = get_kit_body("\"№%@\",")
   auth_token = get_auth_token()

   response_201(kit_body, auth_token)

"""
    TEST 6

    Descripción:
    Se permiten espacios: kit_body = { "name": " A Aaa " }

    Resultado esperado:
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
"""
def test_create_new_kit_name_space_get_success_response():
   
   kit_body = get_kit_body(" A Aaa ")
   auth_token = get_auth_token()

   response_201(kit_body, auth_token)

"""
    TEST 7

    Descripción:
    Se permiten números: kit_body = { "name": "123" }

    Resultado esperado:
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
"""
def test_create_new_kit_name_numbers_get_success_response():
   
   kit_body = get_kit_body("123")
   auth_token = get_auth_token()

   response_201(kit_body, auth_token)

"""
    TEST 8

    Descripción:
    El parámetro no se pasa en la solicitud: kit_body = { }

    Resultado esperado:
    Código de respuesta: 400
"""
def test_create_new_kit_name_no_key_name_get_error_response():
    
    kit_body = data.kit_body.copy()

    kit_body.pop("name")

    auth_token = get_auth_token()

    response_400(kit_body, auth_token)

"""
    TEST 9

    Descripción:
    Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }

    Resultado esperado:
    Código de respuesta: 400
"""
def test_create_new_kit_name_different_types_get_error_response():

    kit_body = get_kit_body(123)

    auth_token = get_auth_token()

    response_400(kit_body, auth_token)