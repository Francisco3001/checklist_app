document.addEventListener("DOMContentLoaded", cargarItems);

async function cargarItems() {
  const res = await fetch("/item");
  const data = await res.json();
  const lista = document.getElementById("listaItems");
  lista.innerHTML = "";

  if (!res.ok) {
    alert(data.error || "Error al cargar items");
    return;
  }

  data.items.forEach(item => {
    const card = document.createElement("li");
    card.className = "item-card";
    card.id = `item-${item.id}`;

    const fecha = new Date(item.fecha_creacion).toLocaleString();

    card.innerHTML = `
      <div class="view-mode" id="view-${item.id}">
        <div>
          <span class="edit-toggle" onclick="toggleEdicion(${item.id})">✏️</span>
        </div>
        <p><strong>📅 Fecha creación:</strong> ${fecha}</p>
        <p><strong>📌 Nombre:</strong> ${item.nombre}</p>
        <p><strong>📝 Descripción:</strong> ${item.descripcion}</p>
        <p><strong>✅ Completado:</strong> ${item.completado ? "Sí" : "No"}</p>
      </div>

      <div class="edit-mode" id="edit-${item.id}" style="display: none;">
        <label>📌 Nombre:</label>
        <input type="text" id="nombre-${item.id}" value="${item.nombre}">

        <label>📝 Descripción:</label>
        <textarea id="descripcion-${item.id}">${item.descripcion}</textarea>

        <label>
          <input type="checkbox" id="check-${item.id}" ${item.completado ? "checked" : ""}>
          Marcar como completado
        </label>

        <div class="controls">
          <button onclick="guardarItem(${item.id})">Guardar</button>
          <button onclick="eliminarItem(${item.id})" style="background:#e74c3c">Eliminar</button>
          <button onclick="toggleEdicion(${item.id})" style="background:#95a5a6">Cancelar</button>
        </div>
      </div>
    `;

    lista.appendChild(card);
  });
}

async function crearItem() {
  const nombre = document.getElementById("nombreInput").value;
  const descripcion = document.getElementById("descripcionInput").value;

  const res = await fetch("/item", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({nombre, descripcion})
  });

  if (res.ok) {
    document.getElementById("nombreInput").value = "";
    document.getElementById("descripcionInput").value = "";
    cargarItems();
  } else {
    const data = await res.json();
    alert(data.error || "Error al crear item");
  }
}

function guardarItem(id) {
  const nombre = document.getElementById(`nombre-${id}`).value;
  const descripcion = document.getElementById(`descripcion-${id}`).value;
  const completado = document.getElementById(`check-${id}`).checked;

  fetch("/item", {
    method: "PUT",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      id_item: id,
      nombre,
      descripcion,
      completado
    })
  })
  .then(() => cargarItems());
}

function eliminarItem(id) {
  fetch("/item", {
    method: "DELETE",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({id_item: id})
  })
  .then(() => cargarItems());
}

function toggleEdicion(id) {
  const view = document.getElementById(`view-${id}`);
  const edit = document.getElementById(`edit-${id}`);

  const isHidden = edit.style.display === "none";
  view.style.display = isHidden ? "none" : "block";
  edit.style.display = isHidden ? "block" : "none";
}
