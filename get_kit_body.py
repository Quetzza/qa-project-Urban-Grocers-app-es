import data

def get_kit_body(name):

    current_body = data.kit_body.copy()

    current_body["name"] = name

    return current_body