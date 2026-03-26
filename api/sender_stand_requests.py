import requests
import env

def get_docs():
    return requests.get(url=(env.URL_SERVICE + env.DOC_PATH))

def get_logs():
    return requests.get(url=(env.URL_SERVICE + env.LOG_MAIN_PATH),params={"count":20})

def get_table(table_name):
    return requests.get(url=(env.URL_SERVICE + f"{env.TABLE_PATH}/{table_name}.csv" ))

def post_new_user(body, header):
    return requests.post(url=(env.URL_SERVICE + env.CREATE_USER_PATH),json=body,headers=header)

def post_products_kit(body, header):
    return requests.post(url=(env.URL_SERVICE + env.PRODUCTS_KITS_PATH),json=body, headers=header)

def post_new_kit_by_user(body, header):
    return requests.post(url=(env.URL_SERVICE + env.KITS_PATH),json=body,headers=header)