from helpers.get_user_body import get_user_body
from assertions.user import positive, negative

def test_create_user_two_letter_in_first_name_get_success_response():
    user = get_user_body('Aa')
    positive.user_successfully(user)

def test_create_user_15_letter_in_first_name_get_success_response():
    user = get_user_body("Aaaaaaaaaaaaaaa")
    positive.user_successfully(user)

def test_create_user_1_letter_in_first_name_get_error_response():
    user = get_user_body("A") 
    negative.symbol(user)

def test_create_user_16_letter_in_first_name_get_error_response():
    user = get_user_body("Aaaaaaaaaaaaaaaa") 
    negative.symbol(user)

def test_create_user_has_space_in_first_name_get_error_response():
    user = get_user_body("A Aaa") 
    negative.symbol(user)

def test_create_user_has_special_symbol_in_first_name_get_error_response():
    user = get_user_body("\"№%@\",")
    negative.symbol(user)

def test_create_user_has_number_in_first_name_get_error_response():
    user = get_user_body("123")
    negative.symbol(user)

def test_create_user_no_first_name_get_error_response():
    user = get_user_body('Aa')
    user.pop("firstName") 
    negative.no_firstname(user)

def test_create_user_empty_first_name_get_error_response():
    user = get_user_body("") 
    negative.no_firstname(user)

def test_create_user_number_type_first_name_get_error_response():
    user = get_user_body(12)
    negative.type(user)