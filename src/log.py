from api_hotel import create_app
from api_hotel.models import Room, Booking
from api_hotel.serializers import serialize_room, serialize_booking
from api_hotel.utils import is_room_available
from datetime import datetime


app = create_app()


def get_available_rooms():
    data = request.get_json()
    arrival_date = datetime.strptime(data['date_arrivee'], '%Y-%m-%d')
    departure_date = datetime.strptime(data['date_depart'], '%Y-%m-%d')
    rooms = Room.query.all()
    if len(rooms) == 0:
        return jsonify([])
    bookings = Booking.query.all()
    availables_rooms = []
    if len(bookings) == 0:
        return jsonify(
            [serialize_room(room) for room in rooms]
        )
    room_bookings = []
    for room in rooms:
        room_bookings.append(room.bookings.all())
        # We know it works

        for booking in room_bookings:
            if arrival_date <= booking.arrival_date:
                continue
            availables_rooms.append(room)

    return jsonify(
        [serialize_room(room) for room in rooms if room not in availables_rooms]
    )




with app.app_context():

    arrival_date = datetime.strptime("2024-03-20", '%Y-%m-%d')
    departure_date = datetime.strptime("2024-03-24", '%Y-%m-%d')
    room_bookings = []
    bookings = Booking.query.all()
    rooms = Room.query.all()
    for room in rooms:
        print(f"_______# is room {room.id} available #_______")
        print(is_room_available(room, arrival_date, departure_date))
        for booking in room.bookings:
            print("----booking----")
            print(serialize_booking(booking))
            print("----arrival_date----")
            print(arrival_date)
            print("----booking.departure_date----")
            print(booking.departure_date)
            print("----booking.arrival_date----")
            print(booking.arrival_date)
            print("----departure_date----")
            print(departure_date)

