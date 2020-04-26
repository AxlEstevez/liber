// --------------------------------------------------------
// Archivo: main.js
// Objetivo: Generar métodos para la interacción de un
// usuario con la interfaz de la aplicación (frint-end).
// Autor: Axl Estevez axlestevez@hotmail.com
// --------------------------------------------------------

// --------------------------------------------------------
// Método: showHide.
// Parámetros: ninguno
// Retorna: nada
// objetivo: Muestra u oculta la contraseña al usuario en
// el input de contraseña.
// --------------------------------------------------------
function showHide() {
  var input = document.getElementById("password");
  var button = document.getElementById("eye");

  if (input.type == "password") {
    input.type = "text";
    button.className = "icon-eye-off";
  } else {
    input.type = "password";
    button.className = "icon-eye";
  }
}

function validationForm() {
  $usuario = document.getElementById("usuario");
  $password = document.getElementById("password");

  if ($usuario.value == "Axl" && $password.value == "Hola") {
    alert("Usuario valido");
  } else {
    alert("Usuario no  valido");
  }
}
