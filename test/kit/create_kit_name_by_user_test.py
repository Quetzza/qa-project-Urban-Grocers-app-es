from helpers.get_kit_body import get_kit_body
from helpers.get_user_token import get_auth_token
from assertions.kit import positive,negative

def test_create_new_kit_name_1_character_get_success_response():
    kit = get_kit_body("a")
    auth_token = get_auth_token()
    positive.get_success_response_201(kit, auth_token)

def test_create_new_kit_name_511_character_get_success_response():
    kit = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" \
    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" \
    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcda" \
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda" \
    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" \
    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    auth_token = get_auth_token()
    positive.get_success_response_201(kit, auth_token)

def test_create_new_kit_name_0_character_get_error_response():
    kit = get_kit_body("")
    auth_token = get_auth_token()
    negative.get_error_response_400(kit, auth_token)

def test_create_new_kit_name_512_character_get_error_response():

    kit = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" \
    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" \
    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
    "abcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc" \
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    auth_token = get_auth_token()
    negative.get_error_response_400(kit, auth_token)

def test_create_new_kit_name_symbol_get_success_response():
   
   kit = get_kit_body("\"№%@\",")
   auth_token = get_auth_token()
   positive.get_success_response_201(kit, auth_token)

def test_create_new_kit_name_space_get_success_response():
   kit = get_kit_body(" A Aaa ")
   auth_token = get_auth_token()
   positive.get_success_response_201(kit, auth_token)

def test_create_new_kit_name_numbers_get_success_response():
   kit = get_kit_body("123")
   auth_token = get_auth_token()
   positive.get_success_response_201(kit, auth_token)

def test_create_new_kit_name_no_key_name_get_error_response():
    kit = get_kit_body("Aaa")
    kit.pop("name")
    auth_token = get_auth_token()
    negative.get_error_response_400(kit, auth_token)

def test_create_new_kit_name_different_types_get_error_response():
    kit = get_kit_body(123)
    auth_token = get_auth_token()
    negative.get_error_response_400(kit, auth_token)
