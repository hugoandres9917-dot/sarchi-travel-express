#poblar_destinos
from __init__ import create_app
from models import db, Destination

app = create_app()

with app.app_context():
    destinos = [
        Destination(name="Arenal Volcano", price_usd=180.0, description="Hot Springs, Canopy, Zip-line, Nature"),
        Destination(name="Guanacaste Beaches", price_usd=220.0, description="Surfing, Resorts, Diving, Fishing"),
        Destination(name="Monteverde Cloud Forest", price_usd=180.0, description="Cloud Forest, Bird watching, Canopy, Wildlife Night Tour"),
        Destination(name="Manuel Antonio National Park", price_usd=180.0, description="Surfing, Wildlife Watching, Beach"),
        Destination(name="Caribbean Coast Tour", price_usd=220.0, description="Tortuguero, Cahuita, Puerto Viejo, Manzanillo"),
        Destination(name="La Paz Waterfalls & Gardens", price_usd=100.0, description="Exotic Animals, Waterfalls, Rainforest"),
        Destination(name="Coffee / Chocolate Tour", price_usd=95.0, description="Grain process, Chocolate making"),
        Destination(name="Poás Volcano National Park", price_usd=120.0, description="Nature, Cloud Forest, Hiking"),
        Destination(name="Tenorio Volcano National Park", price_usd=220.0, description="Cloud Forest, Tubing, Hiking, Horse Riding")
    ]

    db.session.add_all(destinos)
    db.session.commit()
    print("¡Nuevos destinos agregados exitosamente!")