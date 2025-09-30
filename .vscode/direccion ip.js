function validarOcteto(octeto) {
    let valor = parseInt(octeto, 10);
    return valor >= 0 && valor <= 255;
}

function validarDireccionIP(direccionIP) {
    let octetos = direccionIP.split(".");
    if (octetos.length !== 4) {
        return false;
    }
    for (let i = 0; i < octetos.length; i++) {
        if (!validarOcteto(octetos[i])) {
            return false;
        }
    }
    return true;


// Prueba la función con una dirección IP
let direccionIP = "192.168.0.1";
if (validarDireccionIP(direccionIP)) {
    console.log(`La dirección IP ${direccionIP} es válida.`);
} else {
    console.log(`La dirección IP ${direccionIP} no es válida.`);
}
