 verificarDireccionIPv4(ip) {
    // Patrón para una dirección IPv4 válida
    const patron = /^(\d{1,3}\.){3}\d{1,3}$/;
    if (!patron.test(ip)) {
        return false;
    }

    // Verificar que cada octeto esté en el rango de 0 a 255
    const octetos = ip.split('.');
    for (let octeto of octetos) {
        if (parseInt(octeto) < 0 || parseInt(octeto) > 255) {
            return false;
        }
    }
    return true;
}

function categoriaDireccionIPv4(ip) {
    const primerOcteto = parseInt(ip.split('.')[0]);
    if (primerOcteto >= 1 && primerOcteto <= 126) {
        return "Clase A";
    } else if (primerOcteto >= 128 && primerOcteto <= 191) {
        return "Clase B";
    } else if (primerOcteto >= 192 && primerOcteto <= 223) {
        return "Clase C";
    } else if (primerOcteto >= 224 && primerOcteto <= 239) {
        return "Clase D (Multicast)";
    } else if (primerOcteto >= 240 && primerOcteto <= 255) {
        return "Clase E (Experimental)";
    } else {
        return "No especificada";
    }
}

function menu() {
    console.log("Menú:");
    console.log("1. Verificar dirección IPv4");
    console.log("2. Salir");
}

function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    function showMenu() {
        menu();
        rl.question("Elige una opción: ", function(opcion) {
            if (opcion === '1') {
                rl.question("Ingresa la dirección IPv4: ", function(ip) {
                    if (verificarDireccionIPv4(ip)) {
                        const categoria = categoriaDireccionIPv4(ip);
                        console.log(`La dirección IPv4 es válida y pertenece a la ${categoria}.`);
                    } else {
                        console.log("Error: La dirección IPv4 ingresada no es válida.");
                    }
                    showMenu();
                });
            } else if (opcion === '2') {
                console.log("Saliendo del programa...");
                rl.close();
            } else {
                console.log("Opción no válida. Inténtalo de nuevo.");
                showMenu();
            }
        });
    }

    showMenu();
}

main();
