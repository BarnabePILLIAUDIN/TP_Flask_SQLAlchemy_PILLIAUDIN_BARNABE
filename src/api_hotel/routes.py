from flask import Blueprint
from .views import create_room, delete_room, edit_room, \
  delete_booking, run_seeds, get_available_rooms

main = Blueprint('main', __name__)


# Booking routes
main.add_url_rule('/api/reservations/<int:booking_id>', 'delete_booking', delete_booking, methods=['DELETE'])

# Rooms routes
main.add_url_rule('/api/chambres/disponibles', 'get_available_rooms', get_available_rooms, methods=['GET'])
main.add_url_rule('/api/chambres', 'create_room', create_room, methods=['POST'])
main.add_url_rule('/api/chambres/<int:room_id>', 'edit_room', edit_room, methods=['PUT'])
main.add_url_rule('/api/chambres/<int:room_id>', 'delete_room', delete_room, methods=['DELETE'])

# Seeds routes
main.add_url_rule('/api/seeds/<int:number_of_seeds>', 'run_seeds', run_seeds, methods=['POST'])