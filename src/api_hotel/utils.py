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


def get_random_element_of_list(input_list):
    if len(input_list) == 0:
        return None
    return list[randint(0, len(input_list) - 1)]


def is_room_available(room, arrival_date, departure_date):
    for booking in room.bookings:
        if (arrival_date <= booking.departure_date <= departure_date) \
                or (arrival_date <= booking.arrival_date <= departure_date) \
                or (booking.arrival_date <= arrival_date <= booking.departure_date)\
                or (booking.arrival_date <= departure_date <= booking.departure_date):
            return False
    return True
