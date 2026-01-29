import configuration
import requests


"""
    CREA UN NUEVO USUARIO
"""
def post_new_user(body, headers):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=headers)

#print(post_new_user(data.user_body).json()["authToken"]) # d83fb21a-acef-4e53-99fa-b588f7705b9f
"""
    CREAR UN KIT
"""
def post_new_kit(body, headers):

    # headers = data.headers.copy()

    # headers["Authorization"] = "Bearer " + authToken

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json=body, headers=headers)


# result = post_new_user(data.user_body).json()["authToken"]
# post_new_kit(result)