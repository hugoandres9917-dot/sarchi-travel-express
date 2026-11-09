#commands

#Dado que utilizas Faker,
# puedes registrar un comando
# personalizado para cargar
# automáticamente los destinos reales de tu web
# (como el Manuel Antonio National Park. o el Guanacaste Beaches)
# y generar reservas
# de prueba con un solo comando en tu terminal.


# src/commands.py
from faker import Faker
from src.models import db, Destination, Booking

def setup_commands(app):
    @app.cli.command("insert-test-data")
    def insert_test_data():
        db.create_all()
        
        # Lista de destinos reales de Sarchí Travel Express
        destinations_data = [
            {"name": "Arenal Volcano", "price_usd": 180.0, "description": "Hot Springs, Canopy, Zip-line, Nature"},
            {"name": "Guanacaste Beaches", "price_usd": 220.0, "description": "Surfing, Resorts, Diving, Fishing"},
            {"name": "Monteverde Cloud Forest", "price_usd": 180.0, "description": "Cloud Forest, Bird watching, Canopy"},
            {"name": "Manuel Antonio National Park", "price_usd": 180.0, "description": "Surfing, Wildlife Watching, Beach"},
            {"name": "Caribbean Coast Tour", "price_usd": 220.0, "description": "Tortuguero, Cahuita, Puerto Viejo"}
        ]

        for dest in destinations_data:
            existing = Destination.query.filter_by(name=dest["name"]).first()
            if not existing:
                new_dest = Destination(name=dest["name"], price_usd=dest["price_usd"], description=dest["description"])
                db.session.add(new_dest)
        
        db.session.commit()
        print("¡Destinos iniciales agregados correctamente a la base de datos!")