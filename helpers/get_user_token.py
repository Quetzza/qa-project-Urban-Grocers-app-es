from data import user
from data import header
from api import sender_stand_requests

def get_auth_token():

    current_user = user.USER.copy()

    current_header = header.HEADER.copy()

    response = sender_stand_requests.post_new_user(current_user,current_header)

    return response.json()['authToken']