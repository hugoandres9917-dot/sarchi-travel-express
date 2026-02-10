// ==========================
// Script principal
// ==========================

document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.querySelector(".menu-toggle");
  const menu = document.querySelector("nav ul");

  menuToggle.addEventListener("click", () => {
    menu.classList.toggle("active");
  });
});

  // --- Validar fecha (no permitir pasadas) ---
  const dateInput = document.getElementById("date");
  if (dateInput) {
    const today = new Date().toISOString().split("T")[0];
    dateInput.setAttribute("min", today);
  }

  // --- Campo "Other destination" ---
  const destinationSelect = document.getElementById("destination");
  const otherContainer = document.getElementById("other-destination-container");
  const otherInput = document.getElementById("other-destination");

  if (destinationSelect && otherContainer && otherInput) {
    destinationSelect.addEventListener("change", () => {
      if (destinationSelect.value === "Other") {
        otherContainer.style.display = "block";
        otherInput.required = true;
      } else {
        otherContainer.style.display = "none";
        otherInput.required = false;
        otherInput.value = "";
      }
    });
  }

  // --- Confirmación en pantalla al enviar ---
  const form = document.getElementById("bookingForm");
  const successMessage = document.getElementById("form-success");

  if (form && successMessage) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      try {
        const formData = new FormData(form);
        const response = await fetch(form.action, {
          method: form.method,
          body: formData,
          headers: { "Accept": "application/json" }
        });

        if (response.ok) {
          successMessage.style.display = "block";
          form.reset();
          if (otherContainer && otherInput) {
            otherContainer.style.display = "none";
            otherInput.required = false;
          }
        } else {
          alert("❌ Hubo un problema al enviar tu reserva. Intenta nuevamente.");
        }
      } catch (error) {
        console.error("Error al enviar el formulario:", error);
        alert("⚠️ Error de conexión. Intenta más tarde.");
      }
    });
  }

// ==========================
// Función para enviar por WhatsApp
// ==========================
function enviarWhatsApp() {
  const name = document.getElementById("name")?.value || "";
  const contact = document.getElementById("contact")?.value || "";
  const pickup = document.getElementById("pickup")?.value || "";
  const destination = document.getElementById("destination")?.value || "";
  const otherDestination = document.getElementById("other-destination")?.value || "";
  const date = document.getElementById("date")?.value || "";
  const time = document.getElementById("time")?.value || "";

  const finalDestination = destination === "Other" ? otherDestination : destination;
  const companyNumber = "50660530702"; // Número de la empresa

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