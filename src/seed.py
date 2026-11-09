#seed.py

from __init__ import create_app
from models import db, Destination

app = create_app()

with app.app_context():
    # Limpiamos o creamos si es necesario
    d1 = Destination(name="Taller de Carretas Joaquín Chaverri", price_usd=20.0, description="Tradicional fábrica de carretas típicas.")
    d2 = Destination(name="Iglesia de Sarchí", price_usd=10.0, description="Hermosa iglesia de madera con arquitectura única.")
    
    db.session.add_all([d1, d2])
    db.session.commit()
    print("¡Base de datos poblada con éxito!")