from data import user

def get_user_body(name):

    current_body = user.USER.copy()
    
    current_body['firstName'] = name
    
    return current_body