function convertirVelocidad(velocidadEnMetrosPorSegundo) {
    return velocidadEnMetrosPorSegundo * 3.6;
  }
  
  // Solicita al usuario que ingrese una velocidad en m/s
  const velocidadEnMetrosPorSegundo = parseFloat(prompt("Ingresa la velocidad en metros por segundo (m/s): "));
  const velocidadEnKilometrosPorHora = convertirVelocidad(velocidadEnMetrosPorSegundo);
  
  console.log(`${velocidadEnMetrosPorSegundo} m/s es igual a ${velocidadEnKilometrosPorHora} km/h`);
