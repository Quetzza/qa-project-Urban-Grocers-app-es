from api import sender_stand_requests
from data import header

def user_successfully(body):

    current_header = header.HEADER.copy()

    response = sender_stand_requests.post_new_user(body=body,header=current_header)

    assert response.status_code == 201 

    assert response.json()["authToken"] != "" 

    table_response = sender_stand_requests.get_table('user_model')# user_model
   
    str_user = body["firstName"] + "," + body["phone"] + "," + body["address"] + ",,," + response.json()["authToken"]
    
    assert table_response.text.count(str_user) == 1 