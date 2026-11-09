# __init__.py
# Aquí configuramos la conexión a PostgreSQL,
# inicializamos SQLAlchemy y registramos los comandos y rutas.

# src/__init__.py
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from src.extensions import mail  # <-- Importamos mail desde extensions
from src.models import db
from src.routes import api_bp
from src.commands import setup_commands
from flask_cors import CORS

def create_app():
    app = Flask(__name__,
    template_folder="../templates",
    static_folder="../static")
    
    # 1. Habilitar CORS para que tu frontend se comunique con el backend
    CORS(app)
    
    # 2. Configuración de la base de datos y llaves secretas
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        "DATABASE_URL", 
        "postgresql+psycopg2://postgres:Antonella60@localhost:5432/sarchi_travel_db"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "super-secret-key-sarchi")

    # 3. Configuración de Flask-Mail
    # 4. Configuración corregida de Flask-Mail (Usando SSL en el puerto 465)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME", "hugo.andres9917@gmail.com")
    app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD", "xfvu ahac tvcm gvog.")
    app.config['MAIL_DEFAULT_SENDER'] = ("Sarchí Travel Express", os.getenv("MAIL_USERNAME", "hugo.andres9917@gmail.com"))
    # 4. Inicializar base de datos y correo con la app
    db.init_app(app)
    mail.init_app(app)

    # 5. Ruta principal para servir tu página web (index.html)
    @app.route('/', methods=['GET'])
    def serve_frontend():
        return render_template('index.html')
    

    # 6. Registrar las rutas de la API con el prefijo /api
    app.register_blueprint(api_bp, url_prefix='/api')

    # 7. Comandos personalizados
    setup_commands(app)

    return app