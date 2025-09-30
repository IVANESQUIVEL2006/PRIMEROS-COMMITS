function operacionesNumero(cadenaFlotante) {
    // Convertir la cadena flotante a número flotante
    var numeroFlotante = parseFloat(cadenaFlotante);
    
    // Convertir el número flotante a entero
    var numeroEntero = Math.floor(numeroFlotante);
    
    // Realizar operaciones
    var suma = numeroEntero + 10;
    var multiplicacion = numeroEntero * 5;
    var division = numeroEntero / 2;

    // Imprimir resultados
    console.log("Número entero:", numeroEntero);
    console.log("Suma (+10):", suma);
    console.log("Multiplicación (*5):", multiplicacion);
    console.log("División (/2):", division.toFixed(2));
}

// Ejemplo de uso
var cadenaFlotante = "123.45";
operacionesNumero(cadenaFlotante);
