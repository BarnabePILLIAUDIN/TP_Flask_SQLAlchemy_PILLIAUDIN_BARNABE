from flask import Blueprint
from .views import get_available_rooms, create_room, delete_room,edit_room

main = Blueprint('main', __name__)

# Rooms routes 
main.add_url_rule('/api/chambres', 'create_room', create_room, methods=['POST'])
main.add_url_rule('/api/chambres/<int:room_id>', 'edit_room', edit_room, methods=['PUT'])
main.add_url_rule('/api/chambres/<int:room_id>', 'delete_room', delete_room, methods=['DELETE'])