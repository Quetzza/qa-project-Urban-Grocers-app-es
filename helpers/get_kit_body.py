from data import kit

def get_kit_body(name):

    current_kit = kit.KIT.copy()

    current_kit['name'] = name

    return current_kit