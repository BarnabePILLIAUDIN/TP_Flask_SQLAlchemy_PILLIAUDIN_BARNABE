from faker import Faker
from .models import Client, Room, Booking
from .utils import get_random_element_of_list
from .database import db


# Limit the possible types of rooms and status of booking to make the seed more coherent
SEED_TYPE_OF_ROOMS = ['simple', 'double', 'suite', "delux", 'presidentielle']
SEED_STATUS_OF_BOOKING = ['Confirmee', 'annulee', 'En cours de validation']


def create_seed_client():
    return Client(name=Faker().name(), email=Faker().email())


def create_seed_clients(number_of_clients=10):
    return [create_seed_client() for _ in range(number_of_clients)]


def create_seed_room(number):
    return Room(number=number, type=get_random_element_of_list(SEED_TYPE_OF_ROOMS), price=Faker().random_number())


def create_seed_rooms(number_of_rooms=10):
    # We need to make sure the room numbers are unique so we need all the rooms in the db
    rooms = db.session.query(Room).all()
    # We extract the room numbers from the rooms to make it easier to check if a number is already used
    rooms_number = [room.number for room in rooms]
    available_numbers = []
    rooms = []
    while len(available_numbers) < number_of_rooms:
        number = Faker().random_number()
        if number not in rooms_number:
            available_numbers.append(number)
    for number in available_numbers:
        rooms.append(create_seed_room(number))


def create_seed_booking(rooms, clients):
    # We need to have reals rooms and clients to create a booking and have a coherent db
    client = get_random_element_of_list(clients)
    room = get_random_element_of_list(rooms)
    arrival_date = Faker().date()
    departure_date = Faker().date()
    # Make sure the arrival date is before the departure date
    if departure_date < arrival_date:
        arrival_date, departure_date = departure_date, arrival_date
    return Booking(
        client=client,
        room=room,
        arrival_date=arrival_date,
        departure_date=departure_date,
        status=get_random_element_of_list(SEED_STATUS_OF_BOOKING)
    )


def create_seed_bookings(number_of_bookings=10):
    # Make the db query here, so it is run only once
    # We need to have reals rooms and clients to create a booking and have a coherent db
    rooms = db.session.query(Room).all()
    clients = db.session.query(Client).all()
    return [create_seed_booking(rooms, clients) for _ in range(number_of_bookings)]
