from flask import request,jsonify
from sqlalchemy.exc import IntegrityError
from .utils import get_missing_field
from .models import Room
from .database import db
from .serializers import serialize_room


def get_available_rooms():
    return 'get_available_rooms'


def create_room():
    data = request.get_json()
    missing_fields = get_missing_field(data, ['numero', 'type', 'prix'])
    if missing_fields:
        return jsonify({
            "success": False,
            "message" : f'Requette invalide -> Les champs suivants son manquants: {missing_fields}'
                }), 400

    try:
        room = Room(number=data['numero'], type=data['type'], price=data['prix'])
        db.session.add(room)
        db.session.commit()
    except IntegrityError:
        return jsonify({
            "success": False,
            "message" : "Requette invalide -> Cette chambre existe déjà"
        }), 400

    return {
        "success": True,
        "message" : "Chambre ajoutée avec succes",
        "room" : serialize_room(room)
    }

def edit_room(room_id):
    data = request.get_json()
    room = Room.query.get_or_404(room_id)

    for key, value in data.items():
        setattr(room, key, value)

    db.session.commit()

    return jsonify({
        "success": True,
        "message" : "Chambre modifiée avec succes",
        "room" : serialize_room(room)
    })


def delete_room(room_id):
    room = Room.query.get_or_404(room_id)

    db.session.delete(room)
    db.session.commit()

    return {
        "success": True,
        "message" : "Chambre supprimée avec succes",
        "room" : serialize_room(room)
    }
    