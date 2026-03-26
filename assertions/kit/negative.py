from api import sender_stand_requests
from data import header

def get_error_response_400(kit,auth_token):
    current_header = header.HEADER.copy()
    current_header["Authorization"] = f'Bearer {auth_token}'
    response = sender_stand_requests.post_new_kit_by_user(kit,current_header)
    assert response.status_code == 400