#Models (modelos db)
#Aquí unificamos las tablas exactas para guardar los destinos
#que ofreces (como el Arenal Volcano o el Monteverde Cloud Forest)
# y las reservas de los clientes.

# src/models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Destination(db.Model):
    __tablename__ = 'destinations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    price_usd = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    bookings = db.relationship('Booking',backref='destination',lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price_usd": self.price_usd,
            "description": self.description
        }


class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(120),nullable=False)
    client_email = db.Column(db.String(120),nullable=False)
    client_phone = db.Column(db.String(30),nullable=False)
    people_count = db.Column(db.Integer,nullable=False)
    pickup_location = db.Column(db.String(255),nullable=False)
    destination_id = db.Column(db.Integer,db.ForeignKey('destinations.id'),nullable=False)
    travel_date = db.Column(db.Date,nullable=False)
    travel_time = db.Column(db.Time,nullable=False)
    additional_notes = db.Column(db.Text)
    status = db.Column(db.String(50),default="Pending")
    created_at = db.Column(db.DateTime,default=datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "client_name": self.client_name,
            "client_email": self.client_email,
            "people_count": self.people_count,
            "pickup_location": self.pickup_location,
            "destination": self.destination.name if self.destination else None,
            "travel_date": self.travel_date,
            "travel_time": self.travel_time,
            "additional_notes": self.additional_notes,
            "status": self.status,
            "created_at": self.created_at
        }