from random import randint

def get_missing_field(data, fields):
    missing_fields = []
    for field in fields:
        if not data.get(field["name"]):
            missing_fields.append(field["name"])
    return ', '.join(missing_fields)


def check_input_types(data, fields):
    incorrect_fields = []
    for field in fields:
        if data[field["name"]] and not isinstance(data[field["name"]], field["type"]):
            incorrect_fields.append(field["name"])
    return ', '.join(incorrect_fields)


def get_random_element_of_list(list):
    if len(list) == 0:
        return None
    return list[randint(0, len(list) - 1)]