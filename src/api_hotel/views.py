from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from .utils import get_missing_field, check_input_types, is_room_available
from .models import Room, Booking
from .database import db
from .serializers import serialize_room, serialize_booking, serialize_client
from .seeds import create_seed_clients, create_seed_rooms, create_seed_bookings

CREATE_ROOMS_FIELDS = [
    {
        "name": "numero",
        "type": int,
        "required": True,
    },
    {
        "name": "type",
        "type": str,
        "required": True,
    },
    {
        "name": "prix",
        "type": float,
        "required": True,
    }
]


def get_available_rooms():
    data = request.get_json()
    arrival_date = datetime.strptime(data['date_arrivee'], '%Y-%m-%d')
    departure_date = datetime.strptime(data['date_depart'], '%Y-%m-%d')
    rooms = Room.query.all()
    if len(rooms) == 0:
        return jsonify([])
    availables_rooms = []
    for room in rooms:
        if is_room_available(room, arrival_date, departure_date):
            availables_rooms.append(room)

    return jsonify(
        [serialize_room(room) for room in availables_rooms]
    )


def run_client_seeds(number_of_seeds):
    try:
        clients = create_seed_clients(number_of_seeds) 
        db.session.add_all(clients)
        db.session.commit()
        return clients
    except IntegrityError:
        # If the fake data is not good for the db, we try again
        # Most of the time it's because the room number is already used, so we can afford to try again
        # because it will quickly find a unique number as it's unlikely to have a lot of rooms in the db.
        run_client_seeds(number_of_seeds)


def run_room_seeds(number_of_seeds):
    try:
        rooms = create_seed_rooms(number_of_seeds)
        db.session.add_all(rooms)
        db.session.commit()
        return rooms
    except IntegrityError:
        run_room_seeds(number_of_seeds)


def run_booking_seeds(number_of_seeds):
    try:
        bookings = create_seed_bookings(number_of_seeds)
        db.session.add_all(bookings)
        db.session.commit()
        return bookings
    except IntegrityError:
        run_booking_seeds(number_of_seeds)


# Create me a function populate_db that create 10 rows for each class o the model. Please make data coherent,
# and use faker to have better data
def run_seeds(number_of_seeds):
    # Check if the number of seeds is valid
    # We limit it to 10 to avoid adding too much data and struggling with the unique constraints
    if number_of_seeds < 1 or number_of_seeds > 10:
        return jsonify({
            "success": False,
            "message": "Requette invalide -> Le nombre de donnees à ajouter doit être superieur à 0 et moins de 10"
        }), 400

    try:
        clients = run_client_seeds(number_of_seeds)
        rooms = run_room_seeds(number_of_seeds)
        bookings = run_booking_seeds(number_of_seeds)
    except Exception:
        return jsonify({
            "success": False,
            "message": "Erreur lors de l'ajout des donnees"
        }), 500

    return jsonify({
        "success": True,
        "message": "Donnees ajoutees avec succes",
        "clients": [serialize_client(client) for client in clients],
        "rooms": [serialize_room(room) for room in rooms],
        "bookings": [serialize_booking(booking) for booking in bookings]
    })


def delete_booking(booking_id):
    try:
        # get_or_404 method is great but returns that the routes doesn't exist,
        # but here we want to specify that it's the booking doesn't exist
        booking = Booking.query.get(booking_id)
        serialized_booking = serialize_booking(booking)
    except Exception:
        return jsonify({
            "success": False,
            "message": "Reservation introuvable"
        }), 404

    db.session.delete(booking)
    db.session.commit()

    return jsonify(
        {
            "success": True,
            "message": "Reservation supprimee avec succes",
            "booking": serialized_booking
        }
    
    )


def create_room():
    data = request.get_json()
    missing_fields = get_missing_field(data, CREATE_ROOMS_FIELDS)
    if missing_fields:
        return jsonify({
            "success": False,
            "message": f'Requette invalide -> Les champs suivants son manquants: {missing_fields}'
                }), 400
    wrong_fields = check_input_types(data, CREATE_ROOMS_FIELDS)
    if wrong_fields:
        return jsonify({
            "success": False,
            "message": f"Requette invalide -> Les champs suivants n'ont pas le bon type: {wrong_fields}"
        }), 400

    try:
        room = Room(number=data['numero'], type=data['type'], price=data['prix'])
        db.session.add(room)
        db.session.commit()
    except IntegrityError:
        return jsonify({
            "success": False,
            "message": "Requette invalide -> Cette chambre existe dejà"
        }), 400

    return {
        "success": True,
        "message": "Chambre ajoutee avec succes",
        "room": serialize_room(room)
    }


def edit_room(room_id):
    data = request.get_json()
    try:
        room = Room.query.get(room_id)
        serialized_room = serialize_room(room)
    except Exception:
        return jsonify({
            "success": False,
            "message": "Chambre introuvable"
        }), 404

    for key, value in data.items():
        setattr(room, key, value)

    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Chambre modifiee avec succes",
        "room": serialized_room
    })


def delete_room(room_id):
    try:
        room = Room.query.get(room_id)
        serialized_room = serialize_room(room)
    except Exception:
        return jsonify({
            "success": False,
            "message": "Chambre introuvable"
        }), 404

    db.session.delete(room)
    db.session.commit()

    return {
        "success": True,
        "message": "Chambre supprimee avec succes",
        "room": serialized_room
    }
    