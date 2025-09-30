// Autor: Jesús Iván Esquivel Ruiz
// Descripción: Este programa realiza suma, resta, multiplicación y división de números.
// Fecha de creación: 27/02/2025
// Última modificación: 27/02/2025

function obtenerNumeros() {
    try {
        const a = parseFloat(prompt("Ingrese el primer número: "));
        const b = parseFloat(prompt("Ingrese el segundo número: "));
        if (isNaN(a) || isNaN(b)) {
            throw new Error("Entrada inválida. Por favor, ingrese números válidos.");
        }
        return [a, b];
    } catch (error) {
        alert("⚠️ " + error.message);
        return null;
    }
}

function obtenerVariosNumeros() {
    try {
        const numeros = prompt("Ingrese los números separados por comas: ");
        const listaNumeros = numeros.split(',').map(num => {
            const n = parseFloat(num.trim());
            if (isNaN(n)) throw new Error("Entrada inválida. Por favor, ingrese números válidos.");
            return n;
        });
        return listaNumeros;
    } catch (error) {
        alert("⚠️ " + error.message);
        return null;
    }
}

function menu() {
    const operaciones = {
        sumar: (a, b) => a + b,
        sumarVarios: (...nums) => nums.reduce((sum, num) => sum + num, 0),
        restar: (a, b) => a - b,
        multiplicar: (a, b) => a * b,
        multiplicarVarios: (...nums) => nums.reduce((product, num) => product * num, 1),
        dividir: (a, b) => {
            if (b === 0) throw new Error("La división por cero no está permitida.");
            return a / b;
        }
    };

    alert("Calculadora de Operaciones Básicas\n¡Bienvenido! ¿En qué te puedo ayudar hoy?");
    let continuar = true;

    while (continuar) {
        const opcion = prompt(
            "Seleccione una opción (1-7):\n" +
            "1️⃣. Sumar dos números\n" +
            "2️⃣. Sumar varios números\n" +
            "3️⃣. Restar dos números\n" +
            "4️⃣. Multiplicar dos números\n" +
            "5️⃣. Multiplicar varios números\n" +
            "6️⃣. Dividir dos números\n" +
            "7️⃣. Salir"
        );

        try {
            switch (opcion) {
                case '1': {
                    const [a, b] = obtenerNumeros() || [];
                    if (a !== undefined && b !== undefined) {
                        alert(`Resultado: ${operaciones.sumar(a, b)}`);
                    }
                    break;
                }
                case '2': {
                    const numeros = obtenerVariosNumeros();
                    if (numeros) {
                        alert(`Resultado: ${operaciones.sumarVarios(...numeros)}`);
                    }
                    break;
                }
                case '3': {
                    const [a, b] = obtenerNumeros() || [];
                    if (a !== undefined && b !== undefined) {
                        alert(`Resultado: ${operaciones.restar(a, b)}`);
                    }
                    break;
                }
                case '4': {
                    const [a, b] = obtenerNumeros() || [];
                    if (a !== undefined && b !== undefined) {
                        alert(`Resultado: ${operaciones.multiplicar(a, b)}`);
                    }
                    break;
                }
                case '5': {
                    const numeros = obtenerVariosNumeros();
                    if (numeros) {
                        alert(`Resultado: ${operaciones.multiplicarVarios(...numeros)}`);
                    }
                    break;
                }
                case '6': {
                    const [a, b] = obtenerNumeros() || [];
                    if (a !== undefined && b !== undefined) {
                        alert(`Resultado: ${operaciones.dividir(a, b)}`);
                    }
                    break;
                }
                case '7': {
                    alert("¡Hasta luego! ¡Que tengas un buen día!");
                    continuar = false;
                    break;
                }
                default:
                    alert("⚠️ Opción no válida, por favor seleccione una opción del 1 al 7.");
            }
        } catch (error) {
            alert("⚠️ " + error.message);
        }
    }
}

// Ejecutar el menú
menu();
