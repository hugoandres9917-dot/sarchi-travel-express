#sarchi travel express

import tkinter as tk
from tkinter import ttk, messagebox

# Función para enviar la reserva
def enviar_reserva():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    telefono = entry_telefono.get()
    fecha = entry_fecha.get()
    destino = combo_destino.get()
    mensaje = text_mensaje.get("1.0", tk.END)

    # Aquí podrías guardar en base de datos o enviar por correo
    confirmacion = (
        f"Nombre: {nombre}\n"
        f"Correo: {correo}\n"
        f"Teléfono: {telefono}\n"
        f"Fecha: {fecha}\n"
        f"Destino: {destino}\n"
        f"Comentarios: {mensaje}"
    )
    messagebox.showinfo("Reserva confirmada", confirmacion)

# Ventana principal
root = tk.Tk()
root.title("Sarchí Travel Express")
root.geometry("500x600")

# Título
titulo = tk.Label(root, text="¡Bienvenidos a Costa Rica!", font=("Montserrat", 16, "bold"), fg="green")
titulo.pack(pady=10)

subtitulo = tk.Label(root, text="Paraíso Natural y Biodiversidad", font=("Arial", 12))
subtitulo.pack(pady=5)

# Formulario
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Nombre completo:").pack(anchor="w")
entry_nombre = tk.Entry(frame, width=40)
entry_nombre.pack()

tk.Label(frame, text="Correo electrónico:").pack(anchor="w")
entry_correo = tk.Entry(frame, width=40)
entry_correo.pack()

tk.Label(frame, text="Teléfono:").pack(anchor="w")
entry_telefono = tk.Entry(frame, width=40)
entry_telefono.pack()

tk.Label(frame, text="Fecha del tour (YYYY-MM-DD):").pack(anchor="w")
entry_fecha = tk.Entry(frame, width=40)
entry_fecha.pack()

tk.Label(frame, text="Destino:").pack(anchor="w")
destinos = [
    "Parque Nacional Marino Ballena",
    "Parque Nacional Manuel Antonio",
    "Volcán Poás",
    "Volcán Arenal",
    "Caribe Sur: Cahuita / Puerto Viejo"
]
combo_destino = ttk.Combobox(frame, values=destinos, width=37)
combo_destino.pack()

tk.Label(frame, text="Comentarios adicionales:").pack(anchor="w")
text_mensaje = tk.Text(frame, height=5, width=40)
text_mensaje.pack()

# Botón de enviar
btn_enviar = tk.Button(frame, text="Enviar Reserva", bg="green", fg="white", command=enviar_reserva)
btn_enviar.pack(pady=10)

# Ejecutar ventana
root.mainloop()