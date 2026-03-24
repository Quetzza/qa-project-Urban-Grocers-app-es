import config.configuration as configuration
import requests


"""
    CREA UN NUEVO USUARIO
"""
def post_new_user(body, headers):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=headers)

"""
    CREAR UN KIT
"""
def post_new_client_kit(body, headers):

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json=body, headers=headers)
