## run_insert.py
from __init__ import create_app
from models import db
# Importa aquí tu función de inserción o comandos si lo deseas, 
# o ejecuta directamente la lógica de población de Faker:

app = create_app()

with app.app_context():
    print("¡Contexto de Flask cargado con éxito!")
    # Si tienes tu script de inserción aquí, puedes llamarlo, por ejemplo:
    # from src.commands import insert_data
    # insert_data()