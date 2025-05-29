async function logIn() {
  const email = document.getElementById("loginEmail").value;
  const contraseña = document.getElementById("loginPassword").value;

  const res = await fetch("/login", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({email, contraseña})
  });

  const data = await res.json();

  if (res.ok) {
    alert("Sesión iniciada");
    document.cookie = "token=" + data.token + "; path=/";
    window.location.href = "/indexchecklist";
  } else {
    alert(data.error || "Error al iniciar sesión");
  }
}

async function register() {
  const nombre = document.getElementById("registerNombre").value;
  const apellido = document.getElementById("registerApellido").value;
  const email = document.getElementById("registerEmail").value;
  const contraseña = document.getElementById("registerPassword").value;

  const res = await fetch("/register", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({nombre, apellido, email, contraseña})
  });

  const data = await res.json();

  if (res.ok) {
    alert("Registrado correctamente. Ahora podés iniciar sesión.");
  } else {
    alert(data.error || "Error al registrarse");
  }
}
