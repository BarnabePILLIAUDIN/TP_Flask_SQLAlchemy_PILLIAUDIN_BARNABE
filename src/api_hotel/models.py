from .database import db
from .constants import STATUS_OF_BOOKING


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    bookings = db.relationship('Booking', backref='client', lazy=True)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    bookings = db.relationship('Booking', backref='room', lazy=True)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    arrival_date = db.Column(db.DateTime, nullable=False)
    departure_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(
        db.Enum(*STATUS_OF_BOOKING, name='status_of_booking'),
        default='en cours de validation',
        nullable=False
    )
