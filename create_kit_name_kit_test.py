import positive_test
import negative_test
"""
    TEST 1
"""
def test_create_new_kit_name_1_character_get_success_response():
    positive_test.positive_assert("a")

"""
    TEST 2
"""
# def test_create_new_kit_name_511_character_get_success_response():
#     positive_test.positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

"""
    TEST 3
"""
# def test_create_new_kit_name_0_character_get_error_response():
#     negative_test.negative_assert_characters_is_less_than_the_lower_limit("")

"""
    TEST 4
"""
# def test_create_new_kit_name_512_character_get_error_response():
#     negative_test.negative_assert_characters_is_less_than_the_lower_limit("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

"""
    TEST 5
"""
def test_create_new_kit_name_symbol_get_success_response():
    positive_test.positive_assert("\"№%@\",")

"""
    TEST 6
"""
def test_create_new_kit_name_space_get_success_response():
    positive_test.positive_assert(" A Aaa ")

"""
    TEST 7
"""
def test_create_new_kit_name_numbers_get_success_response():
    positive_test.positive_assert("123")

"""
    TEST 8
"""
def test_create_new_kit_name_no_key_name_get_error_response():
    negative_test.negative_assert_no_key_name()