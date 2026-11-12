// ==========================
// Script principal para Sarchí Travel Express
// ==========================

document.addEventListener("DOMContentLoaded", () => {
  // --- Menú hamburguesa ---
  const menuToggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector("nav");

  if (menuToggle && nav) {
    menuToggle.addEventListener("click", () => {
      nav.classList.toggle("active");
    });
  }

  // --- Validar fecha (no permitir fechas pasadas) ---
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
});

// ==========================
// Función para enviar por WhatsApp (Opcional)
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
  const companyNumber = "50662787703"; // Número oficial

  const message = `Shuttle Booking Request:\n\n👤 Name: ${name}\n📧 Contact: ${contact}\n📍 Pickup: ${pickup}\n🎯 Destination: ${finalDestination}\n📅 Date: ${date}\n⏰ Time: ${time}`;

  const url = `https://wa.me/${companyNumber}?text=${encodeURIComponent(message)}`;
  window.open(url, "_blank");
}