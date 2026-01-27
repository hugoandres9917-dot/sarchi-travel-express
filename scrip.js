
// Evitar fechas pasadas en el campo "date"
document.addEventListener("DOMContentLoaded", () => {
  const today = new Date().toISOString().split("T")[0];
  document.getElementById("date").setAttribute("min", today);

  // Mostrar campo "Other destination" si se selecciona "Other"
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
});

// Función para WhatsApp
function enviarWhatsApp() {
  const name = document.getElementById("name").value;
  const contact = document.getElementById("contact").value;
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