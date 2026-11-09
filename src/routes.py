# routes (rutas/logica_de_negocio)

# Aquí manejamos las peticiones para consultar los destinos
# disponibles o registrar una nueva reserva directamente desde
# el formulario de tu página web.

# src/routes.py
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Blueprint, jsonify, request, render_template
from src.models import db, Destination, Booking

api_bp = Blueprint('api', __name__)

def enviar_correos_reserva(body, destination_name):
    client_name = body.get('client_name')
    client_email = body.get('client_email')
    people_count = body.get('people_count')
    pickup_location = body.get('pickup_location')
    custom_destination = body.get('custom_destination')
    travel_date = body.get('travel_date')
    travel_time = body.get('travel_time')
    additional_notes = body.get('additional_notes', 'Ninguna')

    destino_final = f"Personalizado: {custom_destination}" if custom_destination else destination_name

    remitente = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")

    # Mensaje Administrador
    msg_admin = MIMEMultipart()
    msg_admin['From'] = remitente
    msg_admin['To'] = remitente
    msg_admin['Subject'] = f"🚐 ¡Nueva Reserva Recibida! - {client_name}"
    cuerpo_admin = f"""
¡Has recibido una nueva solicitud de servicio de transporte!

👤 Cliente: {client_name}
📧 Contacto: {client_email}
👥 Pasajeros: {people_count}
📍 Origen (Pickup): {pickup_location}
🎯 Destino: {destino_final}
📅 Fecha: {travel_date}
⏰ Hora: {travel_time}
📝 Notas adicionales: {additional_notes}
    """
    msg_admin.attach(MIMEText(cuerpo_admin, 'plain'))

    # Mensaje Cliente
    msg_client = None
    if client_email:
        msg_client = MIMEMultipart()
        msg_client['From'] = remitente
        msg_client['To'] = client_email
        msg_client['Subject'] = "Shuttle Booking Confirmation - Sarchí Travel Express"
        cuerpo_client = f"""
Hello {client_name},

Thank you for booking with us! We have received your request and will contact you shortly to confirm your details.

Here is a summary of your trip request:
- Pickup Location: {pickup_location}
- Destination: {destino_final}
- Date: {travel_date}
- Time: {travel_time}
- Passengers: {people_count}

Best regards,
Sarchí Travel Express
        """
        msg_client.attach(MIMEText(cuerpo_client, 'plain'))

    # Envío seguro utilizando with para evitar bloqueos de socket en Windows
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(remitente, password)
            servidor.sendmail(remitente, remitente, msg_admin.as_string())
            if msg_client:
                servidor.sendmail(remitente, client_email, msg_client.as_string())
        print("✅ ¡Correos enviados exitosamente!")
    except Exception as e:
        print(f"⚠️ Aviso: La reserva se guardó en BD, pero el correo falló por restricción de red: {str(e)}")

@api_bp.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([d.serialize() for d in destinations]), 200

@api_bp.route('/bookings', methods=['GET'])
def get_bookings():

    bookings = Booking.query.all()
    return jsonify([b.serialize() for b in bookings]), 200

@api_bp.route('/health')
def health():
    return jsonify({"status": "online","service": "Sarchi Travel Express"}), 200


@api_bp.route('/bookings/<int:id>', methods=['GET'])
def get_booking(id):

    booking = db.session.get(Booking, id)

    if booking is None:
        return jsonify({"error": "Booking not found"}), 404

    return jsonify(booking.serialize()), 200

@api_bp.route('/bookings', methods=['POST'])
def create_booking():
    body = request.get_json()
    
    if not body:
        return jsonify({"error": "No input data provided"}), 400
        
    required_fields = ['client_name', 'client_email', 'people_count', 'pickup_location', 'destination_id', 'travel_date', 'travel_time']
    for field in required_fields:
        if field not in body:
            return jsonify({"error": f"Missing field: {field}"}), 400

    destination_id = body['destination_id']
    destination = db.session.get(Destination, destination_id)
    if not destination:
        return jsonify({"error": f"Destination with id {destination_id} does not exist"}), 400
    

    new_booking = Booking(
        client_name=body['client_name'],
        client_email=body['client_email'],
        people_count=body['people_count'],
        pickup_location=body['pickup_location'],
        destination_id=body['destination_id'],
        travel_date=body['travel_date'],
        travel_time=body['travel_time'],
        additional_notes=body.get('additional_notes', ''),
        status="Pending"
    )

    db.session.add(new_booking)
    db.session.commit()

    # Intentamos enviar el correo
    enviar_correos_reserva(body, destination.name)

    return jsonify({"message": "Booking created successfully!", "booking": new_booking.serialize()}), 201