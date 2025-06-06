document.getElementById("apoieBtn").onclick = function () {
  document.getElementById("apoieModal").style.display = "block";
};

document.querySelector(".close").onclick = function () {
  document.getElementById("apoieModal").style.display = "none";
};

window.onclick = function (event) {
  const modal = document.getElementById("apoieModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

document.querySelector(".menu-btn").addEventListener("click", function () {
  var menu = document.querySelector(".menu-content");
  menu.style.display = menu.style.display === "block" ? "none" : "block";
});

function atualizarHoraUTC() {
  const agora = new Date();
  // Hora local
  const horasLocais = agora.getHours().toString().padStart(2, "0");
  const minutosLocais = agora.getMinutes().toString().padStart(2, "0");
  const segundosLocais = agora.getSeconds().toString().padStart(2, "0");
  // Hora UTC
  const horas = agora.getUTCHours().toString().padStart(2, "0");
  const minutos = agora.getUTCMinutes().toString().padStart(2, "0");
  const segundos = agora.getUTCSeconds().toString().padStart(2, "0");
  const horaFormatada = `${horas}:${minutos}:${segundos} UTC`;
  document.getElementById(
    "horaLocal"
  ).textContent = `Hora Local: ${horasLocais}:${minutosLocais}:${segundosLocais}`;
  document.getElementById("horaUTC").textContent = `Hora UTC: ${horaFormatada}`;
}

setInterval(atualizarHoraUTC, 1000);
atualizarHoraUTC();
