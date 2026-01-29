import positive_test
import negative_test

def positive_assert(name):
    print(name)

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