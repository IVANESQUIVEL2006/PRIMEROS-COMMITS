function convertirYOperar(cadena) {
   Intentamos convertir la cadena a un número entero
  const numero = parseInt(cadena);

  // Verificamos si la conversión fue exitosa
  if (!isNaN(numero)) {
    // Si es un número, realizamos una operación (en este caso, lo multiplicamos por 2)
    const resultado = numero * 2;
    console.log("El resultado de la operación es:", resultado);
  } else {
    // Si no es un número, mostramos un mensaje de error
    console.error("Error: El valor ingresado no es un número entero válido.");
  }
}

// Pedimos al usuario que ingrese un valor
const valorIngresado = prompt("Ingrese un valor:");

// Llamamos a la función para convertir y operar
convertirYOperar(valorIngresado);