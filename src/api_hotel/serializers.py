def serialize_room(room):
    return {
        'id': room.id,
        "number": room.number,
        'price': room.price,
        "type": room.type
    }


def serialize_client(client):
    return {
        'id': client.id,
        "name": client.name,
        'email': client.email
    }


def serialize_booking(booking):
    return {
        'id': booking.id,
        "arrival_date": booking.arrival_date,
        'departure_date': booking.departure_date,
        "status": booking.status,
        "room": serialize_room(booking.room),
        "client": serialize_client(booking.client)
    }