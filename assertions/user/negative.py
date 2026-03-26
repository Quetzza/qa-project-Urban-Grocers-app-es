from api import sender_stand_requests
from data import header 

def symbol(body):

    current_header = header.HEADER.copy()

    response = sender_stand_requests.post_new_user(body=body, header=current_header)

    assert response.status_code == 400

    assert response.json()["code"] == 400

    assert response.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."

def no_first_name(body):

    current_header = header.HEADER.copy()

    response = sender_stand_requests.post_new_user(body=body,header=current_header)

    assert response.status_code == 400

    assert response.json()["code"] == 400

    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

def type(body):

    current_header = header.HEADER.copy()
    
    response = sender_stand_requests.post_new_user(body=body,header=current_header)

    assert response.status_code == 400

    assert response.json()["code"] == 400