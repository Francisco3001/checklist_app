document.addEventListener("DOMContentLoaded", async () => {
  const res = await fetch("/item");
  const data = await res.json();

  if (!res.ok) {
    alert("Error al cargar datos");
    return;
  }

  const items = data.items;
  const total = items.length;
  const completados = items.filter(i => i.completado).length;
  const pendientes = total - completados;
  const porcentaje = total > 0 ? Math.round((completados / total) * 100) : 0;

  document.getElementById("total").textContent = total;
  document.getElementById("completados").textContent = completados;
  document.getElementById("pendientes").textContent = pendientes;
  document.getElementById("porcentaje").textContent = porcentaje;

  const ctx = document.getElementById("grafico").getContext("2d");
  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["Completados", "Pendientes"],
      datasets: [{
        data: [completados, pendientes],
        backgroundColor: ["#2ecc71", "#e74c3c"],
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: "bottom" },
        title: { display: true, text: "Estado general" }
      }
    }
  });
});
