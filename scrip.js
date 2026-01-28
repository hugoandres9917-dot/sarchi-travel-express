document.addEventListener("DOMContentLoaded", () => {
  // Evitar fechas pasadas
  const today = new Date().toISOString().split("T")[0];
  document.getElementById("date").setAttribute("min", today);

  // Mostrar campo "Other destination"
  const destinationSelect = document.getElementById("destination");
  const otherContainer = document.getElementById("other-destination-container");
  const otherInput = document.getElementById("other-destination");

  destinationSelect.addEventListener("change", function () {
    if (this.value === "Other") {
      otherContainer.style.display = "block";
      otherInput.required = true;
    } else {
      otherContainer.style.display = "none";
      otherInput.required = false;
      otherInput.value = "";
    }
  });

  // Confirmación en pantalla al enviar
  const form = document.getElementById("bookingForm");
  const successMessage = document.getElementById("form-success");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const formData = new FormData(form);
    const response = await fetch(form.action, {
      method: form.method,
      body: formData,
      headers: { 'Accept': 'application/json' }
    });

    if (response.ok) {
      successMessage.style.display = "block";
      form.reset();
      otherContainer.style.display = "none";
      otherInput.required = false;
    } else {
      alert("❌ Hubo un problema al enviar tu reserva. Intenta nuevamente.");
    }
  });
});


// Función para WhatsApp
function enviarWhatsApp() {
  const name = document.getElementById("name").value;
  const contact = document.getElementById("email").value;
  const pickup = document.getElementById("pickup").value;
  const destination = document.getElementById("destination").value;
  const otherDestination = document.getElementById("other-destination").value;
  const date = document.getElementById("date").value;
  const time = document.getElementById("time").value;

  const finalDestination = destination === "Other" ? otherDestination : destination;
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
