import subprocess

def git_command(command):
    """Ejecuta un comando de git y muestra la salida"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

# 1. Agregar todos los cambios
git_command("git add .")

# 2. Hacer commit con un mensaje
mensaje = "Actualización automática desde script en Python"
git_command(f'git commit -m "{mensaje}"')

# 3. Subir a la rama main en GitHub
git_command("git push origin main")
