// Objeto JSON con la configuración
const calcConfig = {
    "emojis": {
        "suma": "➕",
        "resta": "➖",
        "multi": "✖️",
        "div": "➗",
        "igual": "➡️",
        "error": "❌",
        "bienvenida": "👋",
        "despedida": "👾"
    },
    "mensajes": {
        "titulo": "Bienvenido a la Calculadora Profesional v1.0",
        "separador": "==========================================",
        "input1": "Ingrese el primer número: ",
        "input2": "Ingrese el segundo número: ",
        "resultados": "Resultados:",
        "errorNum": "Por favor, ingrese solo números válidos",
        "errorDiv": "No se puede dividir por cero",
        "gracias": "Gracias por usar la calculadora!"
    }
};

// Detectar si estamos en Node.js o navegador
const isNode = typeof process !== 'undefined' && process.versions != null && process.versions.node != null;

let prompt;
if (isNode) {
    // Para Node.js
    const promptSync = require('prompt-sync');
    prompt = promptSync();
} else {
    // Para navegador
    prompt = window.prompt;
}

// Función principal
function calculadora() {
    console.log(`${calcConfig.emojis.bienvenida} ${calcConfig.mensajes.titulo}`);
    console.log(calcConfig.mensajes.separador);

    try {
        // Obtener entrada del usuario
        const num1Input = prompt(calcConfig.mensajes.input1);
        const num2Input = prompt(calcConfig.mensajes.input2);

        // Convertir a números
        const num1 = parseFloat(num1Input);
        const num2 = parseFloat(num2Input);

        // Validar entrada
        if (isNaN(num1) || isNaN(num2)) {
            throw new Error(calcConfig.mensajes.errorNum);
        }

        // Calcular resultados
        const resultados = {
            suma: num1 + num2,
            resta: num1 - num2,
            multiplicacion: num1 * num2,
            division: num2 === 0 ? `${calcConfig.emojis.error} ${calcConfig.mensajes.errorDiv}` : num1 / num2
        };

        // Mostrar resultados
        console.log(`\n${calcConfig.mensajes.resultados}`);
        console.log(calcConfig.mensajes.separador);
        console.log(`${calcConfig.emojis.suma} Suma: ${num1} + ${num2} ${calcConfig.emojis.igual} ${resultados.suma.toFixed(2)}`);
        console.log(`${calcConfig.emojis.resta} Resta: ${num1} - ${num2} ${calcConfig.emojis.igual} ${resultados.resta.toFixed(2)}`);
        console.log(`${calcConfig.emojis.multi} Multiplicación: ${num1} × ${num2} ${calcConfig.emojis.igual} ${resultados.multiplicacion.toFixed(2)}`);
        console.log(`${calcConfig.emojis.div} División: ${num1} ÷ ${num2} ${calcConfig.emojis.igual} ${typeof resultados.division === 'string' ? resultados.division : resultados.division.toFixed(2)}`);

    } catch (error) {
        console.log(`${calcConfig.emojis.error} Error: ${error.message}`);
    }

    console.log(`\n${calcConfig.emojis.despedida} ${calcConfig.mensajes.gracias}`);
}

// Ejecutar
calculadora();