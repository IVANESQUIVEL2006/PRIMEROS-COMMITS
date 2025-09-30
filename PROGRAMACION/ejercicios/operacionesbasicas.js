/**
 * Convierte un número binario a decimal.
 *
 * @param {string} binario - Número en binario.
 * @returns {number} - Número en decimal.
 */
function binarioADecimal(binario) {
    return parseInt(binario, 2);
}

/**
 * Convierte un número octal a decimal.
 *
 * @param {string} octal - Número en octal.
 * @returns {number} - Número en decimal.
 */
function octalADecimal(octal) {
    return parseInt(octal, 8);
}

/**
 * Convierte un número hexadecimal a decimal.
 *
 * @param {string} hexadecimal - Número en hexadecimal.
 * @returns {number} - Número en decimal.
 */
function hexadecimalADecimal(hexadecimal) {
    return parseInt(hexadecimal, 16);
}

/**
 * Convierte un número decimal a binario.
 *
 * @param {number} decimal - Número en decimal.
 * @returns {string} - Número en binario.
 */
function decimalABinario(decimal) {
    return decimal.toString(2);
}

/**
 * Convierte un número decimal a octal.
 *
 * @param {number} decimal - Número en decimal.
 * @returns {string} - Número en octal.
 */
function decimalAOctal(decimal) {
    return decimal.toString(8);
}

/**
 * Convierte un número decimal a hexadecimal.
 *
 * @param {number} decimal - Número en decimal.
 * @returns {string} - Número en hexadecimal.
 */
function decimalAHexadecimal(decimal) {
    return decimal.toString(16);
}

function main() {
    console.log("\n💀 ¡Bienvenido al Conversor de Números! 🎉\n");
    console.log("🇲🇽 Conversiones entre sistemas numéricos binario, octal, decimal y hexadecimal.\n");

    try {
        const numero = prompt("🔢 Ingresa el número: ");
        const sistemaOrigen = parseInt(prompt("\nSelecciona el sistema de origen:\n1. Binario\n2. Octal\n3. Decimal\n4. Hexadecimal\n👉 Opción: "), 10);
        const sistemaDestino = parseInt(prompt("\nSelecciona el sistema de destino:\n1. Binario\n2. Octal\n3. Decimal\n4. Hexadecimal\n👉 Opción: "), 10);

        let decimal;

        switch (sistemaOrigen) {
            case 1:
                decimal = binarioADecimal(numero);
                break;
            case 2:
                decimal = octalADecimal(numero);
                break;
            case 3:
                decimal = parseInt(numero, 10);
                break;
            case 4:
                decimal = hexadecimalADecimal(numero);
                break;
            default:
                console.log("🚫 Sistema de origen inválido.");
                return;
        }

        let resultado;

        switch (sistemaDestino) {
            case 1:
                resultado = decimalABinario(decimal);
                break;
            case 2:
                resultado = decimalAOctal(decimal);
                break;
            case 3:
                resultado = decimal;
                break;
            case 4:
                resultado = decimalAHexadecimal(decimal);
                break;
            default:
                console.log("🚫 Sistema de destino inválido.");
                return;
        }

        console.log(`\n✅ Resultado: ${resultado}`);
    } catch (e) {
        console.log(`\n⚠️ Error: Entrada no válida. ${e.message}`);
    }

    console.log("\n✨ ¡Gracias por usar el Conversor de Números! 🌵🎉");
    console.log("¡Hasta la próxima! 🇲🇽\n");
}

// Llamada a la función principal
main();
