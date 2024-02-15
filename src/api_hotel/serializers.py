def serialize_room(room):
    return {
        'id': room.id,
        "number": room.number,
        'price': room.price,
        "type": room.type
    }