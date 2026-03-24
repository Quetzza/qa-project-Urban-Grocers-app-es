from api import sender_stand_request
from data import data

def get_auth_token():
    
    user_body = data.user_body.copy()

    header = data.headers.copy() 
    
    user_response = sender_stand_request.post_new_user(user_body, header)

    return user_response.json()['authToken']