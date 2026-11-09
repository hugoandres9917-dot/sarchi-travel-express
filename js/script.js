// ==========================
// Script principal
// ==========================
document.addEventListener("DOMContentLoaded", () => {
  // 1. Evitar fechas pasadas en el campo "date"
  const today = new Date().toISOString().split("T")[0];
  const dateInput = document.getElementById("date");
  if (dateInput) {
    dateInput.setAttribute("min", today);
  }

  // 2. Elementos del DOM
  const destinationSelect = document.getElementById("destination");
  const otherContainer = document.getElementById("other-destination-container");
  const otherInput = document.getElementById("other-destination");
  const form = document.getElementById("bookingForm");
  const successMessage = document.getElementById("form-success");

  // 3. Cargar destinos dinámicamente desde la API de Flask (PostgreSQL)
  async function cargarDestinos() {
    try {
      const response = await fetch("http://127.0.0.1:5000/api/destinations");
      const destinations = await response.json();

      if (response.ok && destinationSelect) {
        // Limpiamos y dejamos una opción por defecto
        destinationSelect.innerHTML = '<option value="" disabled selected>Select a destination</option>';
        
        // Recorremos los destinos que vienen de tu BD
        destinations.forEach(dest => {
          const option = document.createElement("option");
          option.value = dest.id; // ¡Guardamos el ID real de PostgreSQL!
          option.textContent = `${dest.name} - $${dest.price_usd}`;
          destinationSelect.appendChild(option);
        });

        // Agregamos la opción "Other" al final por si acaso
        const otherOpt = document.createElement("option");
        otherOpt.value = "Other";
        otherOpt.textContent = "Other / Otro";
        destinationSelect.appendChild(otherOpt);
      }
    } catch (error) {
      console.error("No se pudieron cargar los destinos:", error);
      if (destinationSelect) {
        destinationSelect.innerHTML = '<option value="" disabled selected>Error loading destinations</option>';
      }
    }
  }

  // Ejecutamos la carga al abrir la página
  cargarDestinos();

  // 4. Mostrar u ocultar campo "Other destination"
  if (destinationSelect) {
    destinationSelect.addEventListener("change", function () {
      if (this.value === "Other") {
        otherContainer.style.display = "block";
        if (otherInput) otherInput.required = true;
      } else {
        otherContainer.style.display = "none";
        if (otherInput) {
          otherInput.required = false;
          otherInput.value = "";
        }
      }
    });
  }

  // 5. Envío del formulario a tu API de Flask (PostgreSQL)
  if (form) {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();

      // Preparamos el objeto JSON exacto que espera tu ruta /api/bookings en Flask
      const destinationValue = destinationSelect.value;
      const destinationId = destinationValue === "Other" ? 1 : parseInt(destinationValue);

      const bookingData = {
        client_name: document.getElementById("name").value,
        client_email: document.getElementById("contact").value,
        people_count: parseInt(document.getElementById("people").value),
        pickup_location: document.getElementById("pickup").value,
        destination_id: destinationId,
        custom_destination: destinationValue === "Other" ? otherInput.value : null, // Campo extra si tu BD lo soporta
        travel_date: document.getElementById("date").value,
        travel_time: document.getElementById("time").value,
        additional_notes: document.getElementById("message") ? document.getElementById("message").value : ""
      };


      
      try {
        const response = await fetch("http://127.0.0.1:5000/api/bookings", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
          },
          body: JSON.stringify(bookingData)
        });

        const result = await response.json();

        if (response.ok) {
          if (successMessage) successMessage.style.display = "block";
          form.reset();
          if (otherContainer) otherContainer.style.display = "none";
          if (otherInput) otherInput.required = false;
          cargarDestinos(); // Volvemos a cargar el select
        } else {
          alert("❌ Error: " + (result.error || "No se pudo procesar la reserva."));
        }
      } catch (error) {
        console.error("Error de conexión con el servidor:", error);
        alert("⚠️ Error de conexión con el backend de Flask.");
      }
    });
  }
});

// 6. Función para enviar los datos por WhatsApp (Se mantiene intacta)
function enviarWhatsApp() {
  const name = document.getElementById("name").value;
  const contact = document.getElementById("contact") ? document.getElementById("contact").value : document.getElementById("email").value;
  const pickup = document.getElementById("pickup").value;
  const destinationSelect = document.getElementById("destination");
  const destinationText = destinationSelect.options[destinationSelect.selectedIndex].text;
  const otherDestination = document.getElementById("other-destination").value;
  const date = document.getElementById("date").value;
  const time = document.getElementById("time").value;

  const finalDestination = destinationSelect.value === "Other" ? otherDestination : destinationText;
  const companyNumber = "50660530702";

  const message = `Shuttle Booking Request:\n
👤 Name: ${name}\n
📧 Contact: ${contact}\n
📍 Pickup: ${pickup}\n
🎯 Destination: ${finalDestination}\n
📅 Date: ${date}\n
⏰ Time: ${time}`;

  const url = `https://wa.me/${companyNumber}?text=${encodeURIComponent(message)}`;
  window.open(url, "_blank");
}