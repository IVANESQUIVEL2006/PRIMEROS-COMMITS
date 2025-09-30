function convertirBases() {
    const eleccion = parseInt(document.getElementById("eleccion").value);
    const resultadoDiv = document.getElementById("resultado");
    let inputValor;
    let resultado;
  
    switch (eleccion) {
      case 1: // Binario a octal
        inputValor = parseInt(document.getElementById("inputValor").value);
        if (!validarBinario(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = decimalAOctal(binarioADecimal(inputValor));
        resultadoDiv.textContent = "El octal es " + resultado;
        break;
      case 2: // Binario a decimal
        inputValor = parseInt(document.getElementById("inputValor").value);
        if (!validarBinario(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = binarioADecimal(inputValor);
        resultadoDiv.textContent = "El decimal es " + resultado;
        break;
      case 3: // Binario a hexadecimal
        inputValor = parseInt(document.getElementById("inputValor").value);
        if (!validarBinario(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = decimalAHexadecimal(binarioADecimal(inputValor));
        resultadoDiv.textContent = "El hexadecimal es " + resultado;
        break;
      case 4: // Octal a binario
        inputValor = parseInt(document.getElementById("inputValor").value);
        if (!validarOctal(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = decimalABinario(octalADecimal(inputValor));
        resultadoDiv.textContent = "El binario es " + resultado;
        break;
      case 5: // Octal a decimal
        inputValor = parseInt(document.getElementById("inputValor").value);
        if (!validarOctal(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = octalADecimal(inputValor);
        resultadoDiv.textContent = "El decimal es " + resultado;
        break;
      case 6: // Octal a hexadecimal
        inputValor = parseInt(document.getElementById("inputValor").value);
        if (!validarOctal(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = decimalAHexadecimal(octalADecimal(inputValor));
        resultadoDiv.textContent = "El hexadecimal es " + resultado;
        break;
      case 7: // Decimal a binario
        inputValor = parseInt(document.getElementById("inputValor").value);
        if (!validarDecimal(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = decimalABinario(inputValor);
        resultadoDiv.textContent = "El binario es " + resultado;
        break;
      case 8: // Decimal a octal
        inputValor = parseInt(document.getElementById("inputValor").value);
        if (!validarDecimal(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = decimalAOctal(inputValor);
        resultadoDiv.textContent = "El octal es " + resultado;
        break;
      case 9: // Decimal a hexadecimal
        inputValor = parseInt(document.getElementById("inputValor").value);
        if (!validarDecimal(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = decimalAHexadecimal(inputValor);
        resultadoDiv.textContent = "El hexadecimal es " + resultado;
        break;
      case 10: // Hexadecimal a binario
        inputValor = document.getElementById("inputValor").value.toUpperCase();
        if (!validarHexadecimal(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = decimalABinario(hexadecimalADecimal(inputValor));
        resultadoDiv.textContent = "El binario es " + resultado;
        break;
      case 11: // Hexadecimal a octal
        inputValor = document.getElementById("inputValor").value.toUpperCase();
        if (!validarHexadecimal(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = decimalAOctal(hexadecimalADecimal(inputValor));
        resultadoDiv.textContent = "El octal es " + resultado;
        break;
      case 12: // Hexadecimal a decimal
        inputValor = document.getElementById("inputValor").value.toUpperCase();
        if (!validarHexadecimal(inputValor)) {
          resultadoDiv.textContent = "Número no válido";
          return;
        }
        resultado = hexadecimalADecimal(inputValor);
        resultadoDiv.textContent = "El decimal es " + resultado;
        break;
      default:
        resultadoDiv.textContent = "Elección no válida";
    }
  }
  
  // Validadores
  function validarDecimal(decimal) {
    return true;
  }
  
  function validarBinario(binario) {
    const binarioComoCadena = String(binario);
    for (let i = 0; i < binarioComoCadena.length; i++) {
      const caracter = binarioComoCadena.charAt(i);
      if (caracter !== '0' && caracter !== '1') {
        return false;
      }
    }
    return true;
  }
  
  function validarOctal(octal) {
    const octalComoCadena = String(octal);
    const caracteresOctales = "01234567";
    for (let i = 0; i < octalComoCadena.length; i++) {
      const caracter = octalComoCadena.charAt(i);
      if (caracteresOctales.indexOf(caracter) === -1) {
        return false;
      }
    }
    return true;
  }
  
  function validarHexadecimal(hexadecimal) {
    const caracteresHexadecimales = "0123456789ABCDEF";
    for (let i = 0; i < hexadecimal.length; i++) {
      const caracter = hexadecimal.charAt(i);
      if (caracteresHexadecimales.indexOf(caracter) === -1) {
        return false;
      }
    }
    return true;
  }
  
  // De Decimal a otras bases
  function decimalABinario(decimal) {
    let binario = "";
    while (decimal > 0) {
      binario = (decimal % 2) + binario;
      decimal = Math.floor(decimal / 2);
    }
    return binario;
  }
  
  function decimalAOctal(decimal) {
    let residuo;
    let octal = "";
    const caracteresOctales = ['0', '1', '2', '3', '4', '5', '6', '7'];
    while (decimal > 0) {
      residuo = decimal % 8;
      const caracter = caracteresOctales[residuo];
      octal = caracter + octal;
      decimal = Math.floor(decimal / 8);
    }
    return octal;
  }
  
  function decimalAHexadecimal(decimal) {
    let residuo;
    let hexadecimal = "";
    const caracteresHexadecimales = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];
    while (decimal > 0) {
      residuo = decimal % 16;
      const caracterHexadecimal = caracteresHexadecimales[residuo];
      hexadecimal = caracterHexadecimal + hexadecimal;
      decimal = Math.floor(decimal / 16);
    }
    return hexadecimal;
  }
  
  // Conversiones de otras bases a decimal
  function binarioADecimal(binario) {
    let decimal = 0;
    let potencia = 0;
    const binarioString = String(binario);
    for (let i = binarioString.length - 1; i >= 0; i--) {
      const temp = parseInt(binarioString.charAt(i));
      decimal += temp * Math.pow(2, potencia);
      potencia++;
    }
    return decimal;
  }
  
  function octalADecimal(octal) {
    let decimal = 0;
    let potencia = 0;
    const octalString = String(octal);
    for (let i = oct